from transformers import BartForConditionalGeneration, BartTokenizer
import pandas as pd
import torch

def generate_bart_summary(transcript):
    """
    Generates a summary for a transcript using the BART model.

    Parameters:
        transcript (str): Transcript to summarize.

    Returns:
        str: Generated summary.
    """
    # device = 'cuda' if torch.cuda.is_available() else 'cpu'
    device = 'cpu'
    print("Device: ", device)
    # Load tokenizer
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    # print("Device: ", device)

    # Load model
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    model.to(device)  # Move model to specified device

    # Tokenize the text
    inputs = tokenizer(transcript, return_tensors="pt", max_length=1024, truncation=True, padding="longest")
    inputs = inputs.to(device)  # Move input tensors to specified device

    try:
       # Estimate token length of the transcript
        token_length = inputs.input_ids.size(1)
        max_summary_length = token_length // 2  # Set summary length to half of the estimated token length
        # print("MAX_S_L: ",max_summary_length)

        summary_ids = model.generate(inputs.input_ids, max_length=max_summary_length, num_beams=4, early_stopping=True, min_length=30)

        # Decode and return the summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        print(f"Error processing text: {e}")
        summary = ""

    return summary


# def generate_youtube_transcript_summaries(transcript):
#     """
#     Generates a summary for a YouTube video transcript.

#     Parameters:
#         transcript (str): Transcript text of the YouTube video.

#     Returns:
#         str: Generated summary.
#     """
#     print("Generating summary for YouTube video transcript...")
#     summary = generate_bart_summary(transcript)
#     return summary
def generate_youtube_transcript_summaries(transcript, chunk_size=4096):
    """
    Generates a summary for a YouTube video transcript by processing the transcript in chunks.

    Parameters:
        transcript (str): Transcript text of the YouTube video.
        chunk_size (int): Size of each transcript chunk.

    Returns:
        str: Concatenated summary of all transcript chunks.
    """
    print("Generating summary for YouTube video transcript...")
    
    # Split the transcript into chunks
    transcript_chunks = [transcript[i:i+chunk_size] for i in range(0, len(transcript), chunk_size)]
    # Check the number of chunks
    num_chunks = len(transcript_chunks)
    print("Number of chunks:", num_chunks)
    # Generate summary for each chunk
    summaries = []
    for chunk in transcript_chunks:
        summary = generate_bart_summary(chunk)
        summaries.append(summary)
    
    # Concatenate all summaries
    concatenated_summary = " ".join(summaries)
    
    return concatenated_summary
