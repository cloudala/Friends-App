import pandas as pd
import re

# Adjusting pandas dataframe to display all data
# pd.set_option('display.max_rows', 30)
# pd.set_option('display.max_columns', None)

df = pd.read_csv('friends_quotes.csv')
print(df)

# 1) Finding null values
# Displaying summary of null values in dataset
def show_null_values_summary(df):
    print(df.isnull().sum())

show_null_values_summary(df)
# There are no null values in the file, so we can move on

# 2) Removing the quote order column
df = df.drop('quote_order', axis=1)
print(df)

# 3) Removing episode, which was wrongly transcribed (quotes had character names)
df = df[(df['episode_title'] != 'The Two Parts, Part I')]
print(df)

# 4) Filtering the dataframe to store quotes by the 6 main characters only
def quotes_by_main_characters_only(df, string_columns):
    monica_pattern = r'Monica|MNCA|Monica\s*\([^)]*\)'
    rachel_pattern = r'Rachel|RACH|Rachel\s*\([^)]*\)'
    phoebe_pattern = r'Phoebe|PHOE|Phoebe\s*\([^)]*\)'
    joey_pattern = r'Joey|Joey\s*\([^)]*\)'
    chandler_pattern = r'Chandler|CHAN|Chandler\s*\([^)]*\)'
    ross_pattern = r'Ross|ROSS|Ross\s*\([^)]*\)'
    rows_to_delete = []
    for column in string_columns:
        for index, value in df[column].items():
            monica_match = re.search(monica_pattern, value, re.IGNORECASE)
            rachel_match = re.search(rachel_pattern, value, re.IGNORECASE)
            phoebe_match = re.search(phoebe_pattern, value, re.IGNORECASE)
            joey_match = re.search(joey_pattern, value, re.IGNORECASE)
            chandler_match = re.search(chandler_pattern, value, re.IGNORECASE)
            ross_match = re.search(ross_pattern, value, re.IGNORECASE)
            if monica_match:
                df.at[index, column] = 'Monica'
            elif rachel_match:
                df.at[index, column] = 'Rachel'
            elif phoebe_match:
                df.at[index, column] = 'Phoebe'
            elif joey_match:
                df.at[index, column] = 'Joey'
            elif chandler_match:
                df.at[index, column] = 'Chandler'
            elif ross_match:
                df.at[index, column] = 'Ross'
            else:
                rows_to_delete.append(index)
    df = df.drop(rows_to_delete)
    return df

df = quotes_by_main_characters_only(df, ['author'])
print(df)

# 5) Removing stage directions (didaskalia) from remaining quotes
def cleanup_string_values(df, string_columns):
    for column in string_columns:
        for index, value in df[column].items():
            # Remove text within round brackets
            cleaned_value = re.sub(r'\([^)]*\)', '', value)
            cleaned_value = re.sub(r'\((.*?)\.', '', cleaned_value)
            cleaned_value = re.sub(r'\((.*?)n', '', cleaned_value)
            # Remove text within square brackets
            cleaned_value = re.sub(r'\[[^\]]*\]', '', cleaned_value)
            cleaned_value = re.sub(r'\[(.*?)\.', '', cleaned_value)
            # Remove text within curly brackets
            cleaned_value = re.sub(r'\{[^}]*\}', '', cleaned_value)
            cleaned_value = re.sub(r'\{[^}]*\)', '', cleaned_value)
            # Remove text within angle brackets
            cleaned_value = re.sub(r'<[^>]*>', '', cleaned_value)
            cleaned_value = re.sub(r'>>> Joey\'s Subconscious ', '', cleaned_value)
            cleaned_value = re.sub('’', "'", cleaned_value)
            cleaned_value = re.sub('‘', "'", cleaned_value)
            cleaned_value = re.sub('“', "\"", cleaned_value)
            cleaned_value = re.sub('”', "\"", cleaned_value)
            cleaned_value = re.sub('—', "-", cleaned_value)
            cleaned_value = re.sub('…', '...', cleaned_value)
            cleaned_value = re.sub('\xa0', ' ', cleaned_value)
            cleaned_value = re.sub('\x85', '', cleaned_value)
            cleaned_value = re.sub('\x91', '\'', cleaned_value)
            cleaned_value = re.sub('\x92', '\'', cleaned_value)
            cleaned_value = re.sub('\x93', '\'', cleaned_value)
            cleaned_value = re.sub('\x94', '\'', cleaned_value)
            cleaned_value = re.sub('\x96', '-', cleaned_value)
            cleaned_value = re.sub('\x97', '- ', cleaned_value)
            cleaned_value = re.sub(r'sweatshirt he\'s wearing\.\)', '', cleaned_value)
            cleaned_value = re.sub(r'pain as Monica grabs him underwater\)-', '', cleaned_value)
            cleaned_value = re.sub(r', leans back, and starts reading\.\)', '', cleaned_value)
            cleaned_value = re.sub(r'and Phoebe picks up a wooden baseball bat and starts to swing as Chandler and Monica enter\.\)', '', cleaned_value)
            cleaned_value = re.sub(r'New York\.\)', '', cleaned_value)
            cleaned_value = re.sub(r'jumps away\)-', '', cleaned_value)
            cleaned_value = re.sub(r'She walks around him to the other side\)', '', cleaned_value)
            # Replace multiple white space characters with single space
            cleaned_value = re.sub(r'\s+', ' ', cleaned_value)
            # Strip trailing whitespaces
            cleaned_value = cleaned_value.strip()
            df.at[index, column] = cleaned_value
    return df

df = cleanup_string_values(df, ['quote'])
print(df)

# 6) Displaying rows where quotes contain non-printable characters
def find_nonprintable(s):
    nonprintable_chars = re.findall(r'[^\x20-\x7E\t\n\rèçéÉ]', s)
    return nonprintable_chars, s

# Filter rows where 'quote' column contains non-printable characters
filtered_df = df[df['quote'].apply(lambda x: bool(find_nonprintable(x)[0]))]
print(filtered_df)

# Display the non-printable characters along with the entire string
for index, row in filtered_df.iterrows():
    nonprintable_chars, quote = find_nonprintable(row['quote'])
    print(f"Non-printable characters found in '{row['quote']}': {nonprintable_chars}")

# 7) Removing quotes, which have less than 11 characters in length
df = df[df['quote'].str.len() > 11]
print(df)

# 8) Capitalizing the first letter of every quote
df['quote'] = df['quote'].str.capitalize()

# 9) Capitalizing lowercase characters after punctuation marks and spaces
def capitalize_after_punctuation(s):
    # Replacing i with I (if it is preceded by a space and followed by a space or apostrophy)
    s = re.sub(r'(?<= )[i](?=[ \'`])', 'I', s)
    # Capitalizing the first letter in each quote
    s= re.sub(r'(?<=[.!?]\s)(\w)', lambda m: m.group(1).upper(), s)
    return s

df['quote'] = df['quote'].apply(capitalize_after_punctuation)

# Saving cleaned up dataframe to a new csv file
df.to_csv('friends_quotes_after_cleanup.csv', index=False)