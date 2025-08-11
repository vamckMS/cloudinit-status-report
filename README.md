# CloudInit Epic Status Report Generator

Automated Azure DevOps integration for generating comprehensive CloudInit epic status reports in multiple formats.

## 🚀 Features

- **Azure DevOps Integration**: Direct connection to Azure DevOps using MCP tools
- **Epic Validation**: Validates epics against specific Azure DevOps queries
- **Multiple Report Formats**: Generates Markdown, JSON, and professional Word documents
- **Focused Reporting**: Prioritizes Active epics with detailed child items, separate New epics section
- **Professional Formatting**: Aptos font, tight spacing, color-coded states
- **Child Work Item Tracking**: Complete visibility into epic progress with child items
- **Team Distribution Analysis**: Clear assignment overview and workload distribution

## 📁 Project Structure

```
├── README.md                           # This file
├── .gitignore                         # Git ignore rules
│
├── 📊 Report Generation
├── cloudinit_status_report.md         # Generated Markdown report
├── epic_data.json                     # Original epic data
├── epic_data_validated.json           # Validated against Azure DevOps query
│
├── 🛠️ Core Scripts
├── fetch_cloudinit_epics.py          # Base epic fetching (MCP integration)
├── validate_epics.py                 # Epic validation against queries
├── create_focused_report.py          # Main focused Word report generator
├── create_professional_report.py     # Professional Word report generator
└── convert_to_word.py                # Basic Markdown to Word converter
```

## 🎯 Usage

### 1. Epic Validation
Validate epics against your Azure DevOps query:

```bash
python validate_epics.py
```

### 2. Generate Focused Report (Recommended)
Creates prioritized report with Active epics detailed, New epics in simple table:

```bash
python create_focused_report.py
```

### 3. Generate Professional Report
Creates comprehensive report with all epic details:

```bash
python create_professional_report.py
```

## 📊 Report Types

### 🎯 Focused Report (`create_focused_report.py`)
**Perfect for stakeholder meetings and team updates**

- **🟢 Active Epics Section**: Detailed with child items, latest updates, full formatting
- **🟡 New Epics Section**: Simple table format for planning visibility
- **📈 Executive Summary**: Key metrics and team distribution
- **🔗 Query Validation**: Linked to specific Azure DevOps queries

### 📋 Professional Report (`create_professional_report.py`)
**Comprehensive documentation with all details**

- All epics with full details and child items
- Professional formatting throughout
- Complete audit trail

## 🔧 Configuration

### Azure DevOps Query
Update the query ID in `validate_epics.py`:
```python
query_source = "https://msazure.visualstudio.com/One/_queries/query/YOUR_QUERY_ID/"
```

### Project Settings
Modify project details in scripts:
```python
PROJECT = "One"
AREA_PATH = "One\\CloudInit"
ITERATION_PATH = "One\\Bromine"
```

## 📈 Current Epic Breakdown

- **🟢 8 Active Epics**: Primary development focus
- **🟡 13 New Epics**: Planning and backlog items
- **🔴 1 Removed Epic**: Excluded from reports

### Key Active Areas:
- Linux Provisioning Analyzer (LPA) improvements
- Aurora platform migration
- Security enhancements and vulnerability management
- Infrastructure improvements (NVMe naming, container support)

## 🛠️ Dependencies

```bash
pip install python-docx
```

Azure DevOps MCP tools (handled by VS Code extension)

## 📝 Generated Files

- `CloudInit_Status_Report_Focused.docx` - Main focused report
- `epic_data_validated.json` - Validated epic data
- `cloudinit_status_report.md` - Markdown version

## 🚀 Automation

All scripts can be run independently or as part of automated workflows:

1. **Daily/Weekly Updates**: Run `validate_epics.py` → `create_focused_report.py`
2. **Stakeholder Reports**: Use `CloudInit_Status_Report_Focused.docx`
3. **Team Planning**: Reference New epics table for backlog grooming

## 🔄 Next Steps

1. Run scripts to fetch latest epic and child item data
2. Review and update the status report as needed
3. Share the Word document with your team
4. Set up automated scheduling for regular report generation

---

## 📊 Sample Output

The focused report includes:
- **Executive Summary** with key metrics
- **Active Epics** with detailed child items and status
- **New Epics** in clean table format for planning
- **Team Distribution** analysis
- **Professional formatting** ready for presentations

*Generated using Azure DevOps MCP integration*
