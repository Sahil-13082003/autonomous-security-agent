"""
Main entry point for the application
"""
from agent import SecurityAgent
from config import Config
import sys

def main():
    """Main entry point"""
    print("""
╔════════════════════════════════════════════════════════════════════╗
║       🤖 AUTONOMOUS SECURITY INTELLIGENCE AGENT 🤖                 ║
║                                                                    ║
║  Powered by Google Gemini API                                      ║
║  Professional Security Assessment & Vulnerability Detection        ║
╚════════════════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Validate configuration
        Config.validate()
        print("✅ Configuration validated\n")
        
        # Initialize agent
        agent = SecurityAgent()
        
        # Get target
        target = input("🎯 Enter target IP or domain: ").strip()
        if not target:
            target = Config.DEFAULT_TARGET
        
        # Run scan
        results = agent.scan_target(target)
        
        print("\n✨ Reports saved to:")
        print(f"   • HTML: {results['reports']['html']}")
        print(f"   • Text: {results['reports']['text']}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have:")
        print("1. Created .env file with GEMINI_API_KEY")
        print("2. Added your assignment API key")
        print("3. Installed dependencies: pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()
