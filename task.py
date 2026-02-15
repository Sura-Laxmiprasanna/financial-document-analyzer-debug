# Importing libraries and files
from crewai import Task
from agents import financial_analyst, verifier
from tools import search_tool, FinancialDocumentTool

# Initialize the tool properly
# We use the instance 'read_data_tool' from your FinancialDocumentTool class
document_tool = FinancialDocumentTool.read_data_tool

verification = Task(
    description="Check if the document contains financial data for query: {query}",
    expected_output="Verification result with a brief summary.",
    agent=verifier,
    tools=[document_tool], # Use the initialized variable
    async_execution=False
)

analyze_financial_document = Task(
    description="Analyze the financial document based on: {query}",
    expected_output="A detailed financial analysis report.",
    agent=financial_analyst,
    tools=[document_tool],
    async_execution=False,
)

# ... repeat for other tasks using [document_tool]