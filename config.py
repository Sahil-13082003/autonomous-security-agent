"""
Configuration management for Security Agent
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # API Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_MODEL = "gemini-2.5-flash"
    
    # Agent Configuration
    MAX_TOKENS = 2048
    TEMPERATURE = 0.7
    
    # Paths
    REPORTS_DIR = "reports"
    LOGS_DIR = "logs"
    
    # Scanning Configuration
    DEFAULT_TARGET = os.getenv('DEFAULT_TARGET', '192.168.1.1')
    SCAN_TIMEOUT = 30
    
    # Agent System Prompt
    SYSTEM_PROMPT = """You are an expert autonomous security agent. Your role is to:

1. ANALYZE security scan results comprehensively
2. IDENTIFY vulnerabilities with severity levels
3. ASSESS the overall security posture
4. RECOMMEND specific remediation steps
5. PRIORITIZE threats by impact and exploitability

For each vulnerability:
- Name and CVE ID if known
- CVSS Score (1.0-10.0)
- Severity (Critical/High/Medium/Low)
- Description
- Impact
- Remediation steps
- Timeline recommendations

Be thorough, technical, and actionable."""

    @staticmethod
    def validate():
        """Validate configuration"""
        if not Config.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not set. Add it to .env file"
            )
        
        # Create directories if they don't exist
        os.makedirs(Config.REPORTS_DIR, exist_ok=True)
        os.makedirs(Config.LOGS_DIR, exist_ok=True)
