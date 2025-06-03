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
        animate_actions=True
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
        
        當你收到 Researcher 的搜尋結果時，請：
        1. 仔細分析所有收集到的資料
        2. 按重要性和相關性分類
        3. 製作結構化的摘要報告
        4. 標明每個資訊的來源網址
        5. 提出基於資料的見解和建議
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
        如果滿意當前的研究結果，可以總結並給出結論。
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
    print("📝 使用指南：")
    print("• Researcher 會根據你的指示進行網路搜尋")
    print("• Recorder 會整理搜尋結果並製作報告")
    print("• 你可以透過 User Proxy 提供回饋和指示")
    print("• 輸入 'exit' 可結束研究")
    print("=" * 60)
    
    try:
        # 啟動研究團隊
        await Console(research_team.run_stream(
            task="歡迎使用 AutoGen 研究團隊！請告訴我們你想要研究的主題，Researcher 會開始搜集相關資料，Recorder 會整理成報告。"
        ))
    finally:
        # 確保資源正確關閉
        await researcher.close()
        await model_client.close()
        print("\n🔚 研究團隊已關閉，感謝使用！")

if __name__ == "__main__":
    asyncio.run(main()) 