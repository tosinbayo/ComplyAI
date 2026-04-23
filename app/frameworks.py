FRAMEWORKS = {
    "iso27001": {
        "name": "ISO 27001",
        "prompt": "Assess the document against ISO 27001 information security management requirements and identify control gaps."
    },
    "soc2": {
        "name": "SOC 2",
        "prompt": "Assess the document against SOC 2 trust services criteria and identify missing controls or weaknesses."
    },
    "hipaa": {
        "name": "HIPAA",
        "prompt": "Assess the document against HIPAA security and privacy requirements and identify compliance gaps."
    },
    "nist": {
        "name": "NIST CSF",
        "prompt": "Assess the document against the NIST Cybersecurity Framework and identify missing functions, categories, or subcategories."
    },
    "pci_dss": {
        "name": "PCI DSS",
        "prompt": "Assess the document against PCI DSS requirements and identify gaps, risks, and remediation needs."
    },

    # 🔥 NEW FRAMEWORKS

    "eu_ai_act": {
        "name": "EU AI Act",
        "prompt": "Assess the document against the EU AI Act requirements, including risk classification, transparency, data governance, and prohibited practices."
    },
    "nis2": {
        "name": "NIS2",
        "prompt": "Assess the document against NIS2 cybersecurity and risk management requirements, including incident response, governance, and supply chain security."
    },
    "nist_ai_rmf": {
        "name": "NIST AI RMF",
        "prompt": "Assess the document against the NIST AI Risk Management Framework, focusing on governance, mapping, measurement, and management of AI risks."
    }
}
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from app.db.database import Base


class Framework(Base):
    __tablename__ = "frameworks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    prompt = Column(String, nullable=False)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))