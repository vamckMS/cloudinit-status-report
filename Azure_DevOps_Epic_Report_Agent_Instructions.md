# Azure DevOps Epic Report Generation - Agent Instructions

## Overview
These instructions enable an AI agent to generate professional Word reports for any Azure DevOps project by querying epics and their child items, applying consistent formatting, and creating executive-ready documentation.

## Prerequisites
- Access to Azure DevOps MCP tools
- Microsoft Word document generation capabilities (python-docx)
- Project area path or iteration path to filter epics

## Report Generation Instructions

### 1. Data Collection Phase

#### A. Epic Data Retrieval
```
Use MCP Azure DevOps tools to query epics:
- Search for epics using the target project's area path or iteration path
- Filter by area path: "One\{PROJECT_NAME}" (replace {PROJECT_NAME} with actual project)
- Include fields: System.Id, System.Title, System.State, System.AssignedTo, System.Tags
- Exclude epics with state "Removed"
```

#### B. Child Items Retrieval
```
For each active/committed epic:
- Query child work items (Tasks, User Stories, Bugs)
- Include fields: System.Id, System.Title, System.WorkItemType, System.State, System.AssignedTo
- Focus on items that are actively being worked on
```

### 2. Data Processing Rules

#### Epic Classification
- **Active/Committed Epics**: State = "Active" OR "Committed" 
- **New Epics**: State = "New"
- **Other States**: Any other states (Closed, Done, etc.)

#### Epic Enhancement (for Active/Committed only)
- **Last Updated**: Extract most recent change date from epic or child items
- **Salient Points**: Generate 2-3 executive summary points based on:
  - Epic title keywords (security, provisioning, migration, etc.)
  - Presence of blocker keywords (blocked, critical, risk, urgent)
  - Overall progress and status

#### Blocker Detection
```
Keywords indicating blockers/attention needed:
- blocked, blocker, risk, issue, problem
- urgent, critical, vulnerability, security
- Apply warning icon (⚠️) to epic titles when detected
```

### 3. Document Structure Template

#### Document Header
```
Title: "{PROJECT_NAME} Epic Status Report" (Center-aligned, Heading 1)
Metadata: "Generated: {TIMESTAMP} | Source: Live Azure DevOps MCP | Query: {PROJECT_NAME} Epics" (Center-aligned, italic, 10pt)
```

#### Executive Summary Section
```
Heading: "Executive Summary" (Heading 1)
Content: "This report covers {TOTAL_COUNT} {PROJECT_NAME}-related epics from Azure DevOps. 
Active work is distributed across {ACTIVE_COUNT} active/committed epics with detailed child items, 
while {NEW_COUNT} epics are in 'New' state awaiting prioritization and planning."
```

#### Active & Committed Epics Section
```
Heading: "Active & Committed Epics (Detailed View)" (Heading 1)

For each epic (numbered 1, 2, 3...):
1. Epic Title: "{NUMBER}. {EPIC_TITLE} (#{EPIC_ID})" + blocker icon if applicable
   - Font: Aptos, 14pt, Bold, Black
   - No spacing before/after

2. Epic Details: "    State: {STATE} | Assigned: {ASSIGNEE} | Last Updated: {DATE}"
   - Indented, no spacing before/after

3. Key Updates (if available):
   - Heading: "    Key Updates:" (Bold)
   - Bullet points: "        • {SALIENT_POINT}" (2-3 points max)
   - No spacing before/after

4. Child Items Table (if any):
   - Heading: "    Child Items:" (Bold, no spacing)
   - Table with 4 columns: ID | Title | Type & State | Assigned To
   - Blue headers (4472C4) with white text
   - Alternating row colors: Light blue (E8F1FF) and White (FFFFFF)
   - Column widths: 0.8" | 3.5" | 1.5" | 1.5"
   - Row protection: cantSplit = true for all rows
   - No spacing after table
```

#### New Epics Section
```
Heading: "New Epics (Awaiting Prioritization)" (Heading 1)

Table format:
- 3 columns: Epic ID | Title | Assigned To
- Blue headers (4472C4) with white text
- Alternating row colors
- Column widths: 1.0" | 4.5" | 1.8"
- Center-aligned table
```

### 4. Formatting Specifications

#### Font Standards
- **Primary Font**: Aptos throughout entire document
- **Title**: Aptos, varies by section
- **Body Text**: Aptos, 10-11pt
- **Table Text**: Aptos, 10pt

#### Color Palette
- **Epic Titles**: Black (RGB 0,0,0)
- **Table Headers**: Blue background (4472C4), White text (RGB 255,255,255)
- **Alternating Rows**: Light blue (E8F1FF) and White (FFFFFF)
- **Attention Icons**: Use ⚠️ for blockers

#### Spacing Rules
- **Zero spacing** between epic title and details
- **Zero spacing** before "Child Items:" heading
- **Zero spacing** after tables
- **Minimal spacing** throughout for compact layout

#### Table Properties
- **Style**: Table Grid
- **Row Protection**: cantSplit = true (prevents row breaking across pages)
- **Alignment**: Left for child items, Center for new epics
- **Borders**: Standard table grid borders

### 5. Variable Substitution Guide

When adapting for different projects, replace these variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `{PROJECT_NAME}` | Target project name | "CloudInit", "ServiceMesh", "DataPlatform" |
| `{AREA_PATH}` | Azure DevOps area path | "One\CloudInit", "One\ServiceMesh" |
| `{TIMESTAMP}` | Report generation time | "2025-08-27 13:24:59" |
| `{TOTAL_COUNT}` | Total epic count | "21" |
| `{ACTIVE_COUNT}` | Active/committed epic count | "9" |
| `{NEW_COUNT}` | New epic count | "12" |

### 6. MCP Query Examples

#### Basic Epic Query
```
mcp_azure-devops_search_workitem:
  searchText: "Epic"
  project: ["YourProject"]
  workItemType: ["Epic"]
  areaPath: ["One\\{PROJECT_NAME}"]
```

#### Child Items Query
```
mcp_azure-devops_wit_get_work_items_batch_by_ids:
  project: "YourProject"
  ids: [child_item_ids_from_epic_relations]
```

### 7. Report Footer Template

```
Heading: "Report Details" (Heading 1, on new page)

Bullet list:
- Total Epics Analyzed: {TOTAL_COUNT}
- Active/Committed Epics: {ACTIVE_COUNT}
- New Epics: {NEW_COUNT}
- Other States: {OTHER_COUNT}
- Total Child Items: {CHILD_COUNT}
- Report Generation Time: {TIMESTAMP}
- Data Source: Live Azure DevOps via MCP
- Filtering: Child items only shown for Active/Committed epics
- Enhanced Features: Last updated dates and salient points for active epics
- Row Protection: Child items table rows cannot break across pages
- Font: Aptos throughout document
- Icons: Only used for blockers/attention items (⚠️)
```

### 8. Quality Assurance Checklist

Before finalizing the report, verify:
- [ ] All epics filtered correctly by project area path
- [ ] Removed epics excluded from results
- [ ] Active/committed epics have child items (if any exist)
- [ ] Tables use consistent formatting and colors
- [ ] Font is Aptos throughout
- [ ] Spacing is minimal and consistent
- [ ] Page breaks don't split table rows
- [ ] Executive summary reflects actual data
- [ ] File naming follows pattern: `{PROJECT_NAME}_Live_MCP_Report_{YYYYMMDD_HHMMSS}.docx`

### 9. Customization Options

#### For Different Project Types
- **Security Projects**: Emphasize vulnerability and compliance aspects in salient points
- **Infrastructure Projects**: Focus on deployment and operational metrics
- **Product Features**: Highlight user impact and feature completion
- **Platform Projects**: Emphasize scalability and performance improvements

#### Adaptive Salient Points Logic
```
Based on epic title keywords:
- "security|secrets|vulnerability" → Security-focused points
- "performance|optimize|scale" → Performance-focused points  
- "migrate|upgrade|modernize" → Migration-focused points
- "quality|testing|automation" → Quality-focused points
- Default → Generic progress and blocker points
```

### 10. Error Handling

If data is unavailable:
- **No epics found**: Display "No epics found for {PROJECT_NAME} area path"
- **No child items**: Show "No child items currently assigned"
- **MCP connection issues**: Use fallback message and timestamp
- **Missing assignees**: Display as "Unassigned"

## Usage Summary

To generate a report for any project:
1. Replace `{PROJECT_NAME}` with target project name
2. Update area path filter in MCP queries
3. Execute data collection using MCP tools
4. Apply formatting rules consistently
5. Generate Word document with specified filename pattern

This template ensures consistent, professional reports across all Azure DevOps projects while maintaining the high-quality formatting and executive-ready presentation established in the CloudInit template.
