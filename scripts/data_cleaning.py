# example: drop empty rows & trim
df = pd.read_csv(input_path)
df = df.dropna(subset=['customer_id', 'complaint_text'])
df['complaint_text'] = df['complaint_text'].str.strip()
df.to_csv(output_path, index=False)