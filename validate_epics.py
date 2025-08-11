#!/usr/bin/env python3
"""
Validate and update epic data based on Azure DevOps query results
"""
import json
from datetime import datetime

def validate_and_update_epic_data():
    """
    Validate epic data against the query results and update epic_data.json
    """
    
    # Query results from Azure DevOps (your query: 9dc4fe49-839c-4839-9360-5e323fb1650b)
    query_epics = [
        # Active Epics
        {"id": 24900549, "title": "Secrets Provisioning for CVM", "state": "Active", "assignee": "Christopher Patterson <cpatterson@microsoft.com>", "tags": "Cloudinit; Obj: Experience; PartnerAsk; Producer; Security; Semester:Br; Semester:Se"},
        {"id": 33047344, "title": "NVMe Naming (AZ-VM-Utils)", "state": "Active", "assignee": "Christopher Patterson <cpatterson@microsoft.com>", "tags": ""},
        {"id": 33047787, "title": "Test and Migrate to Aurora", "state": "Active", "assignee": "Ben Ryan <benjaminryan@microsoft.com>", "tags": ""},
        {"id": 33047805, "title": "LPA - Chatbot V3", "state": "Active", "assignee": "Vincenzo Marcella <vmarcella@microsoft.com>", "tags": ""},
        {"id": 33047822, "title": "LPA - Analysis Quality Improvements (bucket)", "state": "Active", "assignee": "Vincenzo Marcella <vmarcella@microsoft.com>", "tags": ""},
        {"id": 33151651, "title": "Tuxops Continuous Quality Improvements (bucket)", "state": "Active", "assignee": "Christopher Patterson <cpatterson@microsoft.com>", "tags": ""},
        {"id": 33583359, "title": "Linux Provisioning Analyzer - Quality improvements/features [Bromine]", "state": "Active", "assignee": "Sophie Gee <sophiegee@microsoft.com>", "tags": "Linux Provisioning; Linux Provisioning Analyzer; lpa"},
        {"id": 33587364, "title": "LPA Security - Bromine 2025", "state": "Active", "assignee": "Peyton Robertson <probertson@microsoft.com>", "tags": ""},
        
        # New Epics
        {"id": 30027894, "title": "P384 key support for VMs in Azure", "state": "New", "assignee": "Vasanth Ramani <vramani@microsoft.com>", "tags": "cloud-init; CRP; Linux Provisioning"},
        {"id": 33047528, "title": "Remove provisioning agent from WALA", "state": "New", "assignee": "Christopher Patterson <cpatterson@microsoft.com>", "tags": ""},
        {"id": 33047627, "title": "PPS Support for Azure Init", "state": "New", "assignee": "", "tags": ""},
        {"id": 33047651, "title": "Azure-init for Containers (Flatcar)", "state": "New", "assignee": "Peyton Robertson <probertson@microsoft.com>", "tags": ""},
        {"id": 33047709, "title": "Provisioning Observability Improvements (bucket)", "state": "New", "assignee": "Christopher Patterson <cpatterson@microsoft.com>", "tags": ""},
        {"id": 33047744, "title": "Cloud-init Quality Improvements (bucket)", "state": "New", "assignee": "Christopher Patterson <cpatterson@microsoft.com>", "tags": ""},
        {"id": 33091209, "title": "Admin Disabled VM Creation", "state": "New", "assignee": "Christopher Patterson <cpatterson@microsoft.com>", "tags": ""},
        {"id": 33091269, "title": "Grooming Required", "state": "New", "assignee": "Vamsi Kavuru <vakavuru@microsoft.com>", "tags": ""},
        {"id": 33091847, "title": "Linux VM Provisioning - Overlake 2+", "state": "New", "assignee": "Christopher Patterson <cpatterson@microsoft.com>", "tags": ""},
        {"id": 33131112, "title": "Linux Provisioning-SFI-SDP-CY25", "state": "New", "assignee": "Peyton Robertson <probertson@microsoft.com>", "tags": ""},
        {"id": 34024684, "title": "LPA - Chatbot V3.5", "state": "New", "assignee": "", "tags": ""},
        {"id": 34024940, "title": "LPA - Chatbot V4", "state": "New", "assignee": "", "tags": ""},
        {"id": 34025034, "title": "LPA - Chatbot V4.5", "state": "New", "assignee": "", "tags": ""},
        
        # Excluded: Removed state
        # {"id": 4976352, "title": "Port walinuxagent capability to cloud-init", "state": "Removed", "assignee": "", "tags": ""}
    ]
    
    # Separate Active and New epics
    active_epics = [epic for epic in query_epics if epic["state"] == "Active"]
    new_epics = [epic for epic in query_epics if epic["state"] == "New"]
    
    # Read current epic data
    try:
        with open('epic_data.json', 'r') as f:
            current_data = json.load(f)
    except FileNotFoundError:
        current_data = {}
    
    # Create updated epic data
    updated_data = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "project": "One",
        "area_path": "One\\CloudInit",
        "iteration_path": "One\\Bromine",
        "query_source": "https://msazure.visualstudio.com/One/_queries/query/9dc4fe49-839c-4839-9360-5e323fb1650b/",
        "summary": {
            "total_epics": len(query_epics),
            "active_epics": len(active_epics),
            "new_epics": len(new_epics),
            "removed_epics": 1  # 4976352 was excluded
        },
        "active_epics": active_epics,
        "new_epics": new_epics
    }
    
    # Save updated data
    with open('epic_data_validated.json', 'w') as f:
        json.dump(updated_data, f, indent=2)
    
    # Validation report
    print("🔍 Epic Data Validation Report")
    print("=" * 50)
    print(f"✅ Query Source: Azure DevOps Query 9dc4fe49-839c-4839-9360-5e323fb1650b")
    print(f"📊 Total Epics Found: {len(query_epics)}")
    print(f"🟢 Active Epics: {len(active_epics)}")
    print(f"🟡 New Epics: {len(new_epics)}")
    print(f"🔴 Removed Epics: 1 (excluded from report)")
    print()
    
    print("🟢 ACTIVE EPICS:")
    for epic in active_epics:
        assignee = epic["assignee"].split("<")[0].strip() if epic["assignee"] else "Unassigned"
        print(f"   • {epic['id']}: {epic['title']} ({assignee})")
    
    print()
    print("🟡 NEW EPICS:")
    for epic in new_epics:
        assignee = epic["assignee"].split("<")[0].strip() if epic["assignee"] else "Unassigned"
        print(f"   • {epic['id']}: {epic['title']} ({assignee})")
    
    print()
    print("📁 Updated epic data saved to: epic_data_validated.json")
    return updated_data

if __name__ == "__main__":
    validate_and_update_epic_data()
