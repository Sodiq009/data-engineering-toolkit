df['complaint_length'] = 
df['complaint_text'].str.len()
df['is_billing'] =
df['complaint_text'].str.contains('bill|billing', case=False)