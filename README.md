<div align="center">
  <h1>🤖 Gen AI Handbooks</h1>
  
  <h2>Your Complete 2025 Roadmap to Learning and Practicing Generative AI</h2>
  
  <p>
    <img alt="Learning Path" src="https://img.shields.io/badge/Learning%20Path-2025-blue"/>
    <img alt="Topics" src="https://img.shields.io/badge/Topics-50+-green"/>
    <img alt="Hands-on" src="https://img.shields.io/badge/Approach-Hands--on-orange"/>
    <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow"/>
  </p>

  <p>
    A comprehensive collection of tutorials, samples, and practical examples to master Generative AI,
    <br/>from fundamentals to advanced agentic systems using AWS Bedrock and Strands Agents.
  </p>
</div>

---

## 🎯 What You'll Learn

This repository is your complete guide to mastering Generative AI in 2025. Whether you're a beginner or looking to advance your skills, you'll find structured learning paths, hands-on examples, and real-world applications.

### 🚀 Key Learning Areas

- **🧠 AI Fundamentals**: LLMs, prompt engineering, and model understanding
- **🛠️ Agent Development**: Building intelligent agents with Strands framework
- **🔧 AWS Integration**: Leveraging AWS Bedrock for production AI systems
- **🤝 Multi-Agent Systems**: Orchestrating multiple AI agents for complex tasks
- **📊 Real-World Applications**: Finance, healthcare, data analysis, and more
- **⚡ Advanced Patterns**: RAG, tool usage, structured outputs, and reasoning

---

## 📚 Learning Roadmap 2025

### 🎯 **Phase 1: Foundations (Weeks 1-4)**
```
📖 Fundamentals
├── Understanding LLMs and Generative AI
├── Prompt Engineering Best Practices
├── Model Selection and Configuration
└── Basic Agent Concepts
```

### 🛠️ **Phase 2: Hands-on Development (Weeks 5-12)**
```
🔨 Development Skills
├── Strands Agents Framework
├── AWS Bedrock Integration
├── Tool Integration and Usage
├── Structured Output Handling
└── Agent State Management
```

### 🚀 **Phase 3: Advanced Applications (Weeks 13-20)**
```
🎪 Advanced Patterns
├── Multi-Agent Systems
├── Agentic RAG Implementation
├── Swarm Intelligence
├── Production Deployment
└── Monitoring and Optimization
```

### 🌟 **Phase 4: Specialization (Weeks 21-26)**
```
🎯 Domain Expertise
├── Industry-Specific Applications
├── Custom Tool Development
├── Performance Optimization
└── Research and Innovation
```

---

## 📁 Repository Structure

```
📦 genai-handbooks/
├── 📖 docs/                           # Comprehensive documentation
│   ├── 📚 user-guide/                # Step-by-step learning guides
│   ├── 🔧 api-reference/             # Technical API documentation
│   └── 💡 examples/                  # Code examples and snippets
│
├── 🎓 samples/                        # Complete sample projects
│   ├── 📝 01-tutorials/              # Beginner-friendly tutorials
│   │   ├── 01-fundamentals/          # AI and LLM basics
│   │   ├── 02-multi-agent-systems/   # Agent orchestration
│   │   └── 03-deployment/            # Production deployment
│   │
│   ├── 🏗️ 02-samples/                # Real-world applications
│   │   ├── 01-restaurant-assistant/  # Customer service AI
│   │   ├── 02-scrum-master-assistant/# Project management
│   │   ├── 09-finance-assistant/     # Financial analysis
│   │   ├── 11-personal-finance/      # Personal finance management
│   │   └── 12-medical-document/      # Healthcare document processing
│   │
│   ├── 🔌 03-integrations/           # Third-party integrations
│   │   ├── Amazon-DataProcessing/    # AWS data processing
│   │   ├── tavily/                   # Web search integration
│   │   └── zep-ai/                   # Memory management
│   │
│   ├── 🎨 04-UX-demos/               # User interface examples
│   │   ├── 01-streamlit-template/    # Web app development
│   │   ├── 02-video-games-sales/     # Data visualization
│   │   └── 04-triage-agent/          # Healthcare triage
│   │
│   └── 🧠 05-agentic-rag/            # Advanced RAG patterns
│       ├── 1-corrective-rag-agent/   # Self-correcting RAG
│       ├── 2-adaptive-structured/    # Adaptive retrieval
│       └── 3-unstructure-structured/ # Document processing
│
└── 🤖 strands-agents/                # Strands framework examples
    ├── 🔧 agents/                    # Core agent patterns
    ├── 👥 multi-agent/               # Multi-agent coordination
    ├── 🏗️ providers/                 # Model provider integrations
    └── 🛠️ tools/                     # Custom tool development
```

---

## 🚀 Quick Start Guide

### 1️⃣ **Environment Setup**

```bash
# Clone the repository
git clone https://github.com/yourusername/genai-handbooks.git
cd genai-handbooks

# Set up Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ **Configure AWS Credentials**

```bash
# Set up AWS credentials for Bedrock access
aws configure
# or set environment variables:
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="ap-southeast-1"
```

### 3️⃣ **Run Your First Agent**

```python
# samples/01-tutorials/01-fundamentals/hello-agent.py
from strands import Agent

agent = Agent(
    model="apac.anthropic.claude-sonnet-4-20250514-v1:0",
    system_prompt="You are a helpful AI assistant."
)

response = agent("Hello! Explain what generative AI is in simple terms.")
print(response)
```

### 4️⃣ **Explore Advanced Examples**

```bash
# Try a structured output example
cd strands-agents/agents/structured.output
python index.py

# Run a multi-agent system
cd samples/02-samples/09-finance-assistant-swarm-agent
python main.py

# Test RAG capabilities
cd samples/05-agentic-rag/1-corrective-rag-agent
python corrective_rag.py
```

---

## 🎯 Learning Paths

### 🌱 **Beginner Path: AI Foundations**
Perfect for those new to AI and looking to build a solid foundation.

1. **Week 1-2**: [AI Fundamentals](./samples/01-tutorials/01-fundamentals/)
   - Understanding LLMs and how they work
   - Basic prompt engineering techniques
   - Introduction to AI agents

2. **Week 3-4**: [First Agent Development](./strands-agents/agents/)
   - Setting up your development environment
   - Creating your first Strands agent
   - Understanding agent configuration

### 🚀 **Intermediate Path: Practical Applications**
For developers ready to build real-world AI applications.

1. **Week 1-3**: [Tool Integration](./strands-agents/tools/)
   - Building custom tools for agents
   - Integrating external APIs
   - Handling structured outputs

2. **Week 4-6**: [Real-World Projects](./samples/02-samples/)
   - Restaurant assistant with booking capabilities
   - Personal finance management system
   - Document processing automation

### 🎓 **Advanced Path: Multi-Agent Systems**
For experienced developers building complex AI systems.

1. **Week 1-4**: [Multi-Agent Coordination](./samples/01-tutorials/02-multi-agent-systems/)
   - Agent communication patterns
   - Swarm intelligence implementation
   - Conflict resolution strategies

2. **Week 5-8**: [Production Deployment](./samples/01-tutorials/03-deployment/)
   - Scaling agent systems
   - Monitoring and observability
   - Performance optimization

---

## 🛠️ Key Technologies

<div align="center">

| Technology | Purpose | Learning Priority |
|------------|---------|-------------------|
| **🔷 Strands Agents** | Core agent framework | ⭐⭐⭐⭐⭐ |
| **☁️ AWS Bedrock** | Model hosting & inference | ⭐⭐⭐⭐⭐ |
| **🐍 Python** | Primary development language | ⭐⭐⭐⭐⭐ |
| **📊 Pydantic** | Data validation & schemas | ⭐⭐⭐⭐ |
| **🌐 Streamlit** | Web interface development | ⭐⭐⭐ |
| **🔍 RAG Systems** | Knowledge retrieval | ⭐⭐⭐⭐ |
| **📡 MCP Protocol** | Agent communication | ⭐⭐⭐ |

</div>

---

## 📈 Progress Tracking

### ✅ **Beginner Milestones**
- [ ] Set up development environment
- [ ] Create and run first agent
- [ ] Understand prompt engineering basics
- [ ] Implement simple tool integration
- [ ] Build a basic chat application

### ✅ **Intermediate Milestones**
- [ ] Deploy agent to AWS
- [ ] Implement structured output handling
- [ ] Create custom tools
- [ ] Build a domain-specific assistant
- [ ] Integrate external APIs

### ✅ **Advanced Milestones**
- [ ] Design multi-agent system
- [ ] Implement agentic RAG
- [ ] Deploy production-ready application
- [ ] Optimize for performance and cost
- [ ] Contribute to open-source projects

---

## 🤝 Community & Support

### 💬 **Getting Help**
- 📖 [Documentation](./docs/) - Comprehensive guides and references
- 💡 [Examples](./samples/) - Working code examples
- 🐛 [Issues](https://github.com/yourusername/genai-handbooks/issues) - Report bugs or request features
- 💬 [Discussions](https://github.com/yourusername/genai-handbooks/discussions) - Community Q&A

### 🎯 **Learning Resources**
- 📺 **Video Tutorials**: Step-by-step video guides
- 📝 **Blog Posts**: In-depth technical articles
- 🎪 **Live Demos**: Interactive examples you can run
- 📚 **Best Practices**: Production-ready patterns

### 🌟 **Contributing**
We welcome contributions! See [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for guidelines.

- 🐛 Report bugs and issues
- 💡 Suggest new examples or improvements
- 📖 Improve documentation
- 🔧 Add new sample projects

---

## 🎁 What's Included

### 📚 **50+ Learning Examples**
- Beginner-friendly tutorials with step-by-step instructions
- Real-world applications spanning multiple industries
- Advanced patterns for experienced developers
- Production deployment examples

### 🛠️ **Ready-to-Use Templates**
- Streamlit web applications
- Multi-agent system blueprints
- RAG implementation patterns
- AWS deployment configurations

### 📖 **Comprehensive Documentation**
- API references and guides
- Best practices and patterns
- Troubleshooting and FAQ
- Performance optimization tips

---

## 🗓️ 2025 Learning Schedule

### **Q1 2025: Foundations** 
*January - March*
- Complete fundamentals track
- Build first 3 sample projects
- Master prompt engineering
- Deploy first agent to AWS

### **Q2 2025: Applications**
*April - June*
- Develop 5 domain-specific agents
- Implement RAG systems
- Master tool integration
- Build web interfaces

### **Q3 2025: Advanced Systems**
*July - September*
- Create multi-agent systems
- Implement agentic RAG
- Optimize for production
- Contribute to community

### **Q4 2025: Specialization**
*October - December*
- Focus on chosen domain
- Build portfolio projects
- Share knowledge with community
- Plan 2026 advanced topics

---

## 📊 Success Metrics

Track your progress with these measurable goals:

- **📈 Skills Developed**: 50+ AI/ML concepts mastered
- **🏗️ Projects Built**: 10+ complete applications
- **⚡ Performance**: Sub-second response times
- **💰 Cost Optimization**: 50% reduction in inference costs
- **🤝 Community**: Contributing to open-source projects

---

## 🔮 Future Roadmap

### **Coming in 2025**
- 🧠 Advanced reasoning patterns
- 🌐 Multi-modal agent examples
- 🔄 Continuous learning systems
- 🛡️ AI safety and alignment
- 📱 Mobile AI applications

### **Emerging Technologies**
- Agentic workflows
- Tool-calling optimization
- Memory management systems
- Agent-to-agent protocols
- Edge AI deployment

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <h3>🚀 Ready to Start Your Gen AI Journey?</h3>
  
  <p>
    <a href="./samples/01-tutorials/01-fundamentals/">
      <img src="https://img.shields.io/badge/Start%20Learning-Begin%20Your%20Journey-brightgreen?style=for-the-badge"/>
    </a>
  </p>
  
  <p>
    <strong>⭐ Star this repository if you find it helpful!</strong>
    <br/>
    <em>Join thousands of developers mastering Gen AI in 2025</em>
  </p>
</div>
