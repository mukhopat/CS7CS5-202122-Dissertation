def get_ordinal_encoding_map(series):
    enc_map = series.unique()
    enc_map = dict(enumerate(enc_map.flatten(), 1))
    enc_map = {val: key for key, val in enc_map.items()}
    enc_map['None'] = 0
    return enc_map

enc_map = get_ordinal_encoding_map(df["commit_author_email"])
df["author_code"] = df["commit_author_email"].replace(enc_map)