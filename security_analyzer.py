"""
Security analysis and vulnerability assessment
"""
from datetime import datetime
from typing import Dict, List, Any

class SecurityAnalyzer:
    """Analyzes security vulnerabilities and generates assessments"""
    
    # Common vulnerabilities database
    VULNERABILITY_DB = {
        "OpenSSH_7.4": {
            "name": "OpenSSH Key Exchange Weakness",
            "cve": "CVE-2018-15473",
            "cvss": 7.5,
            "severity": "HIGH",
            "description": "Information disclosure vulnerability in OpenSSH"
        },
        "Apache_2.4.41": {
            "name": "Apache HTTP Server Vulnerabilities",
            "cve": "CVE-2021-26690",
            "cvss": 5.3,
            "severity": "MEDIUM",
            "description": "Mod_proxy_uwsgi buffer overflow vulnerability"
        },
        "MySQL_5.7": {
            "name": "MySQL Remote Access Exposure",
            "cve": "N/A",
            "cvss": 8.0,
            "severity": "HIGH",
            "description": "Publicly accessible database with weak credentials"
        }
    }
    
    def __init__(self):
        self.vulnerabilities: List[Dict[str, Any]] = []
        self.scan_timestamp = datetime.now().isoformat()
    
    def analyze_ports(self, ports: List[Dict]) -> Dict[str, Any]:
        """Analyze open ports for vulnerabilities"""
        analysis = {
            "timestamp": self.scan_timestamp,
            "total_ports": len(ports),
            "open_ports": ports,
            "vulnerabilities": [],
            "risk_score": 0.0
        }
        
        for port_info in ports:
            service = port_info.get("service", "")
            version = port_info.get("version", "")
            
            # Check against vulnerability database
            for app, vuln_data in self.VULNERABILITY_DB.items():
                if app.replace("_", ".") in version or app.replace("_", " ") in version:
                    analysis["vulnerabilities"].append({
                        "port": port_info["port"],
                        "service": service,
                        "version": version,
                        **vuln_data
                    })
        
        # Calculate risk score
        analysis["risk_score"] = self._calculate_risk_score(analysis["vulnerabilities"])
        
        return analysis
    
    def _calculate_risk_score(self, vulnerabilities: List[Dict]) -> float:
        """Calculate overall risk score (0-10)"""
        if not vulnerabilities:
            return 1.0
        
        total_cvss = sum(v.get("cvss", 0) for v in vulnerabilities)
        avg_cvss = total_cvss / len(vulnerabilities)
        
        return min(avg_cvss, 10.0)
    
    def format_analysis(self, analysis: Dict) -> str:
        """Format analysis for readability"""
        output = f"""
╔══════════════════════════════════════════════════════════════════╗
║           SECURITY ANALYSIS REPORT                               ║
╚══════════════════════════════════════════════════════════════════╝

📊 SCAN SUMMARY
├─ Timestamp: {analysis['timestamp']}
├─ Open Ports: {analysis['total_ports']}
├─ Vulnerabilities Found: {len(analysis['vulnerabilities'])}
└─ Overall Risk Score: {analysis['risk_score']:.1f}/10.0

🔴 VULNERABILITIES IDENTIFIED:
"""
        
        for i, vuln in enumerate(analysis['vulnerabilities'], 1):
            output += f"""
{i}. {vuln['name']}
   ├─ Port: {vuln['port']}
   ├─ Service: {vuln['service']}
   ├─ Version: {vuln['version']}
   ├─ CVSS Score: {vuln['cvss']}/10
   ├─ Severity: {vuln['severity']}
   ├─ CVE: {vuln['cve']}
   └─ Description: {vuln['description']}
"""
        
        return output
