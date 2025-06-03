import pandas as pd

# Load both CSV files
df1 = pd.read_csv("myth_query252.csv")
df2 = pd.read_csv("myth_query1358with.csv")

# Standardize columns to have same structure
df1.columns = ["char1Label", "char1Type", "relationLabel", "char2Label", "char2Type"]
df2.columns = ["char1Label", "char1Type", "relationLabel", "char2Label", "char2Type"]

# Combine both files into one DataFrame
df_all = pd.concat([df1, df2], ignore_index=True)

# Create relationships DataFrame
relationships_df = df_all.rename(columns={
    "char1Label": "start_id",
    "char2Label": "end_id",
    "relationLabel": "type"
})[["start_id", "end_id", "type"]].drop_duplicates()

# Create nodes DataFrame
nodes_df = pd.concat([
    df_all[["char1Label", "char1Type"]],
    df_all[["char2Label", "char2Type"]].rename(columns={"char2Label": "char1Label", "char2Type": "char1Type"})
], ignore_index=True).drop_duplicates()

# Rename and reorder columns
nodes_df.columns = ["id", "type"]
nodes_df["label"] = nodes_df["id"]
nodes_df = nodes_df[["id", "label", "type"]]

# Save to CSV
nodes_df.to_csv("nodes.csv", index=False)
relationships_df.to_csv("relationships.csv", index=False)

print("✅ Created: nodes.csv and relationships.csv")
