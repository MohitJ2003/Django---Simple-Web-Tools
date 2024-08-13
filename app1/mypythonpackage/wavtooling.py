import wave
import struct
import os


def split_wav(input_file, output_dir, part_size):
    with wave.open(input_file, 'rb') as wav_file:
        params = wav_file.getparams()
        sample_width = params.sampwidth
        frame_rate = params.framerate
        num_channels = params.nchannels

        frame_per_rate = int((part_size * 1024 * 1024) /
                             (sample_width * num_channels))

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        part_num = 1
        while True:
            frames = wav_file.readframes(frame_per_rate)
            if not frames:
                break

            out_file = os.path.join(output_dir, f'part_{part_num}.wav')
            with wave.open(out_file, 'wb') as part_wav:
                part_wav.setparams(params)
                part_wav.writeframes(frames)

            part_num += 1


"""if __name__ == "__main__":
    path = 'djangoProjects/project1/app1'
    #input_file = 'audiondvideofiles/dristi_hindi_interview.wav'
    input_file = 'audiondvideofiles/yakpktfmep785hindi.wav'
    filename = input_file[18:]
    filename = filename[:-4]
    output_dir = "audioinparts/%s" %filename

    part_size = 10
    split_wav(input_file,output_dir,part_size)
    print("Audio file split into parts successfully.")
"""
