# 🤖 Autonomous Security Intelligence Agent

Professional autonomous security agent powered by Google Gemini AI.

## Features

✨ **Autonomous Decision Making** - AI agent decides scan strategy  
🔍 **Intelligent Vulnerability Detection** - Identifies real CVEs  
📊 **Professional Reports** - Generates HTML and text reports  
⚡ **Real-time Analysis** - Uses Gemini API for intelligence  

## Quick Start

### Installation
```bash
# Install dependencies
pip3 install -r requirements.txt
```

### Setup
```bash
# Create environment file
cp .env.example .env

# Edit .env and add your GEMINI_API_KEY
nano .env
```

### Run Agent
```bash
# Start the security agent
python3 main.py

# Enter target when prompted
# Example: 192.168.1.1
```

## Output

The agent generates:

- **HTML Report** - Beautiful formatted vulnerability assessment
- **Text Report** - Detailed analysis with remediation steps
- **AI Recommendations** - Smart fixes from Gemini
- **Risk Score** - Overall security assessment (0-10)

## Technology Stack

- **Google Gemini 2.5 Flash API** - AI-powered analysis
- **Python 3.8+** - Core language
- **HTML5/CSS3** - Professional reporting

## Project Structure
```
autonomous-security-agent/
├── main.py              # Entry point
├── agent.py            # Core agent logic
├── config.py           # Configuration
├── security_analyzer.py # Vulnerability detection
├── report_generator.py # Report generation
├── requirements.txt    # Dependencies
├── .env.example       # Example environment file
└── reports/           # Generated reports
```

## How It Works

1. **Planning** - Agent decides scanning strategy
2. **Scanning** - Performs security reconnaissance
3. **Analysis** - Identifies vulnerabilities
4. **Reporting** - Generates professional reports
5. **Recommendations** - Provides remediation steps

## Example Workflow
```
$ python3 main.py

🤖 AUTONOMOUS SECURITY INTELLIGENCE AGENT

🎯 Enter target IP or domain: 192.168.1.1

📋 Step 1: Agent Planning Scan Strategy...
✓ Strategy: I recommend scanning ports...

🔍 Step 2: Performing Security Scan...
✓ Scan complete. Found 4 open ports

📊 Step 3: Analyzing Vulnerabilities...
[1] OpenSSH Key Exchange Weakness
    Port: 22
    CVSS: 7.5
    Severity: HIGH

💡 Step 4: Generating AI Recommendations...
✓ Recommendations Generated

📄 Step 5: Generating Reports...
✓ HTML Report: reports/security_report_192_168_1_1_20260326_124400.html
✓ Text Report: reports/security_report_192_168_1_1_20260326_124400.txt

✅ SCAN COMPLETE!
```

## Getting Started

1. Get your free Gemini API key from [aistudio.google.com](https://aistudio.google.com)
2. Clone this repository
3. Install dependencies: `pip3 install -r requirements.txt`
4. Create `.env` file with your API key
5. Run: `python3 main.py`
6. Enter target IP address
7. Review generated reports

## License

MIT

## Author

Sahil Zunjarrao
