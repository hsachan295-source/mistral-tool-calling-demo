from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai.chat_models import ChatMistralAI

from langchain.tools import tool
from datetime import date
from langchain.messages import HumanMessage,ToolMessage,AIMessage

@tool
def get_current_date():
  '''Use this Tool for getting the current date.''' #dot string use kerte function decribe or large model ham kya ker rahe hai
  return str(date.today())

model = ChatMistralAI(model="mistral-small-latest" ).bind_tools([get_current_date]) #model ke sath tools bind karna jishe date bata sake shai

response = model.invoke("What is today's date?") #model se question karna

tool_result = get_current_date.invoke(response.tool_calls[0]['args']) #model ke tool calls print karna

tool_message = ToolMessage(
    content=tool_result,
    tool_call_id=response.tool_calls[0]["id"]
)
second_response = model.invoke([
  HumanMessage("What is today's date?"),
   response,
   tool_message
])
print(second_response.text) 
#yaha hamne tools use kiya hua kyo model jab ahhe work nhi kerte hai tab ham tools use karte hai taki model ko pata chale ki usse kya karna hai aur uske baad hamne tool ka result model ko diya taki model uske basis pe answer de sake