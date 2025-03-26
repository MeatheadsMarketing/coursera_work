# 📊 Module 2: Exploring the Data World

This module focuses on foundational data concepts like data types, sources, and metadata — converted into structured knowledge and deployable AI assistants using the SPG Assistant Builder pipeline.

---

## 🔍 Lessons Processed

- Structured vs Unstructured Data  
- Primary Data Sources  
- Qualitative vs Quantitative Data  
- The Importance of Metadata  

---

## 🤖 Assistant Created

### **Metadata Manager**
- **Purpose:** Classify and manage metadata fields across datasets  
- **Input:** CSV with column headers  
- **Output:** Metadata descriptions, tags, data types, and governance tips  
- **File:** `assistant_metadata_manager.py`  
- **Chained via:** `spg_assistant_map.json`

---

## 📄 Output Files

| File | Description |
|------|-------------|
| `module_cheatsheet.csv` | 30-row SPG-formatted cheat sheet (auto-generated) |
| `spg_assistants.md` | GPT-generated blueprint markdown |
| `spg_starters.py` | GPT-generated starter script for assistant |
| `assistant_metadata_manager.py` | Fully executable assistant |
| `spg_assistant_map.json` | Chaining/registration metadata |
| `README.md` | Module overview & documentation |

---

## 🧪 How to Run This Module

> Run locally with Streamlit:

```bash
streamlit run pages/assistant_metadata_manager.py
