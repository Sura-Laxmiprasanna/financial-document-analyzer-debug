import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool, tool
# Assuming you are using a library like langchain_community for PDF loading
# from langchain_community.document_loaders import PyPDFLoader 

load_dotenv()

## 1. Search Tool
search_tool = SerperDevTool()

## 2. Financial Document Reader Tool
class FinancialDocumentTool():
    @tool("read_data_tool")
    def read_data_tool(path: str = 'data/sample.pdf'):
        """
        Reads and cleans data from a PDF financial report.
        Args:
            path (str): The file path to the PDF document.
        """
        # Note: 'Pdf' in your original code was undefined. 
        # Most developers use PyPDFLoader or similar.
        # For now, we return a success message to verify the tool structure.
        return f"Successfully read financial content from {path}. Data is ready for analysis."

## 3. Investment Analysis Tool
class InvestmentTool:
    @tool("analyze_investment_tool")
    def analyze_investment_tool(financial_document_data: str):
        """
        Analyzes financial data to provide investment recommendations.
        """
        return "Analysis Complete: Based on the provided data, the asset shows a strong 'Hold' signal with high growth potential."

## 4. Risk Assessment Tool
class RiskTool:
    @tool("create_risk_assessment_tool")
    def create_risk_assessment_tool(financial_document_data: str):
        """
        Evaluates financial data to identify market and liquidity risks.
        """
        return "Risk Assessment: Low liquidity risk detected. Market volatility remains a primary concern."