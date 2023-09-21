import youtube_dl
from youtube_transcript_api import YouTubeTranscriptApi

def get_latest_video_full_sentences(channel_name):
    try:
        # Create a YouTube DL instance to search for the latest video by channel name
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'force_generic_extractor': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(f"ytsearch1:{channel_name}", download=False)
            if 'entries' in result and result['entries']:
                latest_video_id = result['entries'][0]['id']
                
                # Get the captions for the latest video
                captions = YouTubeTranscriptApi.get_transcript(latest_video_id)
                
                # Extract full sentences with timestamps
                sentences_with_timestamps = []
                current_sentence = ""
                start_time = 0

                for caption in captions:
                    text = caption['text']
                    start = caption['start']
                    end = start + caption['duration']

                    # Check if the sentence ends with a full stop
                    if text.endswith('.'):
                        current_sentence += text
                    else:
                        current_sentence += text + ' '

                    if text.endswith('.') or caption == captions[-1]:
                        sentences_with_timestamps.append({
                            'start_time': start_time,
                            'end_time': end,
                            'sentence': current_sentence
                        })
                        current_sentence = ""
                        start_time = end

                return sentences_with_timestamps , latest_video_id
            else:
                return None

    except Exception as e:
        return str(e)

def get_captions():
    # channel_name = input("Enter the YouTube channel name: ")
    l = []
    channel_name = "dhruv rathee"
    sentences_with_timestamps , latest_video_id = get_latest_video_full_sentences(channel_name)
    if type(sentences_with_timestamps) == str:
        raise ValueError(sentences_with_timestamps)
    elif sentences_with_timestamps:
        # print("Full sentences with timestamps for the latest video:")
        for sentence_info in sentences_with_timestamps:
            caption_dict = {"s":None,
                "e":None,
                "sentence":None}
            start_time = sentence_info['start_time']
            end_time = sentence_info['end_time']
            sentence = sentence_info['sentence'].replace('\n', ' ')
            # print(f"{start_time:.2f} - {end_time:.2f}: {sentence}")
            caption_dict["s"]=start_time
            caption_dict["e"]=end_time
            caption_dict["sentence"]=sentence
            l.append(caption_dict)
        return l,latest_video_id
    else:
        print("Unable to fetch full sentences for the latest video.")

if __name__ == "__main__":
    get_captions()
    # print(get_latest_video_full_sentences("dhruv rathee"))
