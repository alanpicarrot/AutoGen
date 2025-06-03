# pip install -U autogen-agentchat autogen-ext[openai,web-surfer]
# playwright install
import asyncio
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.agents.web_surfer import MultimodalWebSurfer

async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    
    # Researcher: 負責網路搜尋和資料收集
    researcher = MultimodalWebSurfer(
        "researcher", 
        model_client, 
        headless=False, 
        animate_actions=True,
        system_message="""你是一個專業的研究員 (Researcher)。
        你的任務是：
        1. 根據用戶的需求進行深入的網路搜尋
        2. 收集相關的資料、數據和資訊
        3. 確保資料的準確性和可靠性
        4. 將收集到的原始資料傳遞給 Recorder 進行整理
        
        搜尋時請注意：
        - 使用多個可靠的資料源
        - 記錄資料來源的網址
        - 收集具體的數據和事實
        """
    )
    
    # Recorder: 負責彙整和記錄研究資料
    recorder = AssistantAgent(
        "recorder",
        model_client=model_client,
        system_message="""你是一個專業的記錄員 (Recorder)。
        你的任務是：
        1. 接收 Researcher 收集的原始資料
        2. 將資料進行分類、整理和摘要
        3. 建立結構化的報告
        4. 突出重點和關鍵發現
        5. 提供清晰的結論和建議
        
        整理時請：
        - 按主題分類資訊
        - 標明資料來源
        - 提供摘要和詳細分析
        - 用清晰的格式呈現
        """
    )
    
    # User Proxy: 負責最終決策和互動
    user_proxy = UserProxyAgent(
        "user_proxy",
        human_input_mode="ALWAYS",
        system_message="""你是用戶代理 (User Proxy)。
        你的職責是：
        1. 審核 Recorder 整理的研究報告
        2. 決定是否需要更多資料或不同角度的研究
        3. 提供最終的決策和指導
        4. 與用戶進行互動
        
        如果需要結束研究，請輸入 'exit'。
        如果需要更多研究，請明確指出需要什麼資訊。
        """
    )
    
    # 設定終止條件：當用戶輸入 'exit' 時結束
    termination = TextMentionTermination("exit", sources=["user_proxy"])
    
    # 建立研究團隊：Researcher → Recorder → User Proxy 的順序
    research_team = RoundRobinGroupChat(
        [researcher, recorder, user_proxy], 
        termination_condition=termination,
        max_turns=20  # 設定最大回合數避免無限循環
    )
    
    print("=" * 60)
    print("🔬 AutoGen 研究團隊已啟動")
    print("=" * 60)
    print("團隊成員：")
    print("📊 Researcher - 負責網路搜尋和資料收集")
    print("📝 Recorder - 負責彙整和記錄研究資料")
    print("👤 User Proxy - 負責最終決策和互動")
    print("=" * 60)
    print("輸入 'exit' 可結束研究")
    print("=" * 60)
    
    try:
        # 啟動研究團隊
        await Console(research_team.run_stream(
            task="請開始進行研究。Researcher 請根據用戶需求搜集資料，Recorder 負責整理，User Proxy 做最終決策。"
        ))
    finally:
        # 確保資源正確關閉
        await researcher.close()
        await model_client.close()
        print("\n🔚 研究團隊已關閉，感謝使用！")

if __name__ == "__main__":
    asyncio.run(main()) 