import os
import wave
import traceback
import speech_recognition as sr
import assemblyai as aai
from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
from pydub.playback import play
from pytube import YouTube

import aspose.pdf as ap
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import moviepy.editor
import tkinter as tk
from tkinter import ttk
import time
from tqdm import tqdm

import yt_dlp

base_path = os.path.dirname(os.path.abspath(__file__)).split("djangoProjects")[0].replace("\\","/")+"djangoProjects/"

def extractepname(
        filename=base_path + "project1/app1/mytextfiles/yakepsname1to814.txt"):
    epdetailfile = open(filename, "r")
    epnamefile = open(
        base_path + "project1/app1/mytextfiles/yakeplist.txt", "w")
    for fileline in epdetailfile:
        if fileline[:2] == "Ep":
            epnamefile.write(fileline)
            # print(fileline)
        if 'nowLocked' in fileline:
            pass

    print("New episode titles has been written to yakeplist.txt : ")
    epnamefile.close()
    epdetailfile.close()


def removespace(word="rewrw", chracter=" "):
    newword = ""
    for alpha in word:
        if not alpha.isspace():
            newword += alpha
    return newword


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


def extarctaudio(video_file_path, audio_file_path, nameofaudiofile):
    # Load the Video
    # video = moviepy.editor.VideoFileClip("krishna.mp4")
    video = moviepy.editor.VideoFileClip(video_file_path)
    # Extract the Audio
    audio = video.audio
    audio.write_audiofile(audio_file_path + f"/{nameofaudiofile}" + ".wav")


def createfilename(link, shortfilename="yakshinipktfm"):
    num = ""
    numlist = []
    yt = YouTube(link)
    orgvidnm = yt.title
    orgvidnm = removespace(word=orgvidnm)
    video_length = yt.length

    for a in orgvidnm:
        if a.isnumeric():
            if len(num) < 3:
                num += a
                if len(num) == 3:
                    numlist.append(num)
                    num = ""

    epnumlist = sorted(list(set(numlist)))
    for num in range(int(epnumlist[0]) + 1, int(epnumlist[-1]) + 1):
        epnumlist.append(str(num))

    nofepinvideo = (video_length // 810) + 1
    createdfilename = shortfilename
    epnumlist = sorted(list(set(epnumlist)))

    try:
        if video_length < 810 * nofepinvideo:
            for epind in range(nofepinvideo):
                createdfilename += '_' + epnumlist[epind]
            return createdfilename
    except Exception as e:
        createdfilename = shortfilename
        for epnum in epnumlist:
            createdfilename += '_' + epnum
        return createdfilename


# Function to download a YouTube video
def download_video_from_youtube(link, outputdirect, video_name):
    try:
        yt = YouTube(link)
        video = yt.streams.get_lowest_resolution()

        video_name = outputdirect + video_name
        if video_name in os.listdir(outputdirect):
            print(f"{video_name} video is already downloaded !! ")
        else:
            print(f"{video_name} video is downloading....")
            video.download(outputdirect, video_name)
            print(f"{video_name} video is download successfully !! ")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        exc = traceback.print_exc()
        print(exc)


def audiototextbyparts(directory, file_name):
    lst = os.listdir(directory)  # your directory path
    number_files = len(lst)
    sorted_lst = sorted(lst)

    common_filename = sorted_lst[0]
    common_filename = common_filename[:5] + common_filename[6:]
    new_lst = []
    for file_number in range(1, number_files + 1):
        next_new_filename = common_filename[:5] + str(file_number) + common_filename[5:]
        new_lst.append(next_new_filename)

    filename = directory[13:-1]
    filename = file_name
    single_line = ''
    c = 0
    for a in tqdm(new_lst):
        hindi_line = audio_to_text(directory + a)
        if hindi_line == "Speech recognition could not understand the audio":
            single_line += "..................."
            c += 1
        # print(hindi_line)
        else:
            single_line += hindi_line + ' '
        time.sleep(0.1)
    print(filename)
    pdfmaker_3(file_name, single_line)
    print(f"{c} lines are not transcribed")
    print('next Paragraph ')


# Runner Code
# 12:17 PM 8/13/2023
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Record the audio file

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")  # Recognize speech using Google Web Speech API
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"


def get_allepnum_of3digit(pdf_path):
    list1 = os.listdir(pdf_path)
    numlist = []
    num = ""
    # print(list1)
    for a in list1:
        for b in a:
            if b.isnumeric():
                if len(num) < 3:
                    num += b
                    if len(num) == 3:
                        numlist.append(num)
                        num = ""
    epnumlist = sorted(list(set(numlist)))

    return epnumlist


def youtubehindi_link2text(link):
    outputdirect = base_path + "project1/app1/videosdirect/"
    outputdirect_aud = base_path + "project1/app1/audiofiles/"
    listofeppdfdirec = base_path + "project1/app1/static/mypdffiles/"
    audioinpartsdirect = base_path + "project1/app1/audioinparts/"
    outputdirect_aud_mp3 = base_path + "project1/app1/static/audiofiles/"
    listofeppdf = os.listdir(listofeppdfdirec)

    listofep = os.listdir(outputdirect_aud)
    print("\n\nYes Here !!\n\n")
    # filename = "yakshinipktfm_" + str(episodes_num)
    """if episodes_num == 0:
        filename = createfilename(link)
        setlink_and_epname_in_txtfile(link, filename)"""
    filename = createfilename(link)
    newvideoname = filename + '.mp4'
    newwavfilename = filename + ".wav"
    newpdffilename = filename + ".pdf"
    newmp3filename = filename + ".mp3"
    videopath = outputdirect + newvideoname
    download_video_yt_dlp(link,outputdirect, newvideoname)

    print("Checking the episode titles printing to pdf")
    ep_numslist = get_ep_nums(filename)
    print(ep_numslist)
    ep_namelist = getting_nd_beautifying_ep_namelist_2(ep_numslist)
    print(ep_namelist)

    if os.path.isfile(outputdirect_aud + newwavfilename) and os.path.isfile(outputdirect_aud_mp3 + newmp3filename):
        print(f"{newwavfilename} is already present !!")
        print(f"{newmp3filename} is already present !!")
    else:
        print(f"{newwavfilename} is being extracting .....")
        extarctaudio(videopath, outputdirect_aud, filename)
        print(f"{newwavfilename} is extracted successfully !!")

        print(f"{newmp3filename} is being extracting .....")
        extract_audio_mp3(videopath, outputdirect_aud_mp3 + filename + ".mp3")
        print(f"{newmp3filename} is extracted successfully !!")

    if f"{filename}.pdf" not in listofeppdf:
        output_dir = f"{audioinpartsdirect + filename}/"
        part_size = 10
        audiofilepath = outputdirect_aud + filename + '.wav'
        split_wav(audiofilepath, output_dir, part_size)
        print("Audio file split into parts successfully")
        print(f"------------------------Working on {filename}.wav.../----------------------")

        audiototextbyparts(output_dir, newpdffilename)
    else:
        print(f"{filename}.pdf created already")

    print('----------------- All done--------------------')


def extract_audio_mp3(input_video, output_audio):
    try:
        # Load the video clip
        video_clip = VideoFileClip(input_video)

        # Extract audio
        audio_clip = video_clip.audio

        # Save audio as MP3
        audio_clip.write_audiofile(output_audio, codec='mp3')

        print(f"Audio extracted and saved as {output_audio}")

    except Exception as e:
        print(f"Error: {e}")


def getting_nd_beautifying_ep_namelist_2(ep_num_list):
    ep_name_list = []
    epnamefile = open(
        base_path + "project1/app1/mytextfiles/yakeplist.txt", "r")
    for fileline in epnamefile:
        for a in ep_num_list:
            if a in fileline:
                if 'â€¦' in a or 'â€"' in a:
                    new_string = a.replace('â€¦', '...')
                    new_string = new_string.replace('â€“', '-')
                    ep_name_list.append(new_string)
                else:
                    ep_name_list.append(fileline)
    epnamefile.close()

    return ep_name_list


def get_ep_nums(file_name="default_name"):
    numlist = []
    num = ""
    for a in file_name:
        if a.isnumeric():
            if len(num) < 3:
                num += a
                if len(num) == 3:
                    numlist.append(num)
                    num = ""

    epnumlist = sorted(list(set(numlist)))
    return epnumlist


def pdfmaker_3(filename, paragraph_towritten):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add Header

    ep_numslist = get_ep_nums(filename)
    print(ep_numslist)
    ep_namelist = getting_nd_beautifying_ep_namelist_2(ep_numslist)
    print(ep_namelist)
    all_ep_names = ""
    for a in ep_namelist:
        all_ep_names += a

    header = ap.text.TextFragment(all_ep_names)

    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 15
    header.horizontal_alignment = ap.HorizontalAlignment.JUSTIFY
    header.position = ap.text.Position(100, 780)
    page.paragraphs.add(header)

    # Initialize textfragment object
    # Calculate page dimensions
    page_width, page_height = page.rect.width, page.rect.height
    text_fragment = ap.text.TextFragment(f"\n{paragraph_towritten}")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 2
    text_fragment.text_state.font_style.BOLD
    # text_fragment.text_state.word_spacing = 5
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.FULL_JUSTIFY
    # text_fragment.position = ap.text.Position(50, 750)
    text_fragment.text_state

    # Add text fragment to new page
    page.paragraphs.add(text_fragment)

    # Save updated PDF
    document.save(
        base_path + 'project1/app1/static/mypdffiles/' + filename)
    print('------------------------------------Pdf Created Successfully------------------------------------')


def dowload_video_andextractaudio(link):
    outputdirect = base_path + "project1/app1/videosdirect/"
    outputdirect_aud = base_path + "project1/app1/audiofiles/"
    outputdirect_aud_mp3 = base_path + "project1/app1/static" \
                           "/audiofiles/"

    filename = createfilename(link)
    setlink_and_epname_in_txtfile(link, filename)
    newvideoname = filename + '.mp4'
    newwavfilename = filename + ".wav"
    newmp3filename = filename + ".mp3"

    videopath = outputdirect + newvideoname
    download_video_from_youtube(link, outputdirect, newvideoname)

    print("Checking the episode titles printing to pdf")
    ep_numslist = get_ep_nums(filename)
    print(ep_numslist)
    ep_namelist = getting_nd_beautifying_ep_namelist_2(ep_numslist)
    print(ep_namelist)

    # print(os.path.isfile(outputdirect_aud + newwavfilename), os.path.isfile(outputdirect_aud_mp3 + newmp3filename))
    if os.path.isfile(outputdirect_aud + newwavfilename) and os.path.isfile(outputdirect_aud_mp3 + newmp3filename):
        print(f"{newwavfilename} is already present !!")
    else:
        print(f"{newwavfilename} is being extracting .....")
        extarctaudio(videopath, outputdirect_aud, filename)
        print(f"{newwavfilename} is extracted successfully !!")

        print(f"{newmp3filename} is being extracting .....")
        extract_audio_mp3(videopath, outputdirect_aud_mp3 + filename + ".mp3")
        print(f"{newmp3filename} is extracted successfully !!")


def sort_vd_and_link_names():
    a = base_path + "project1/app1/mytextfiles/linklisttext.txt"

    fileob = open(a, 'r', encoding="utf-8")
    l1 = []
    for e in fileob:
        l1.append(e)
        # print(e)

    l2 = sorted(set(l1))
    # print(l2)
    fileob.close()

    fileob = open(a, 'w', encoding="utf-8")
    for e in l2:
        fileob.write(e)
    fileob.close()


def setlink_and_epname_in_txtfile(link, file_name):
    # sort_vd_and_link_names()

    path = base_path + "project1/app1/mytextfiles/linklisttext.txt"

    linkfile = open(path, 'r', encoding="utf-8")
    line = f"Video Youtube Name - {str(file_name)}     Link - {link}"

    for lline in linkfile:
        # print(lline, line)
        lline.replace("\n", "")
        # print(lline == line, lline, line)

        if line == lline:
            print("Link and Video Name already Written to linklisttext.txt")
            break

    else:
        linkfile = open(path, 'a', encoding="utf-8")
        line.replace("\n", "")
        linkfile.write("\n" + line)
        print("Link and Video Name Written to linklisttext.txt")
        linkfile.close()


def youtubehindi_link2text_listwise(listoflinks):
    # print(listoflinks)
    for link in listoflinks:
        outputdirect = base_path + "project1/app1/videosdirect/"
        outputdirect_aud = base_path + "project1/app1/audiofiles/"
        listofeppdfdirec = base_path + "project1/app1/static/mypdffiles/"
        audioinpartsdirect = base_path + "project1/app1/audioinparts/"
        outputdirect_aud_mp3 = base_path + "project1/app1/static/audiofiles/"
        listofeppdf = os.listdir(listofeppdfdirec)
        listofep = os.listdir(outputdirect_aud)

        filename = createfilename(link)
        setlink_and_epname_in_txtfile(link, filename)
        newvideoname = filename + '.mp4'
        newwavfilename = filename + ".wav"
        newpdffilename = filename + ".pdf"
        newmp3filename = filename + ".mp3"
        videopath = outputdirect + newvideoname
        download_video_from_youtube(link,outputdirect,newvideoname)

        print("Checking the episode titles printing to pdf")
        ep_numslist = get_ep_nums(filename)
        print(ep_numslist)
        ep_namelist = getting_nd_beautifying_ep_namelist_2(ep_numslist)
        print(ep_namelist)

        if os.path.isfile(outputdirect_aud + newwavfilename) and os.path.isfile(outputdirect_aud_mp3 + newmp3filename):
            print(f"{newwavfilename} is already present !!")
            print(f"{newmp3filename} is already present !!")
        else:
            print(f"{newwavfilename} is being extracting .....")
            extarctaudio(videopath, outputdirect_aud, filename)
            print(f"{newwavfilename} is extracted successfully !!")

            print(f"{newmp3filename} is being extracting .....")
            extract_audio_mp3(videopath, outputdirect_aud_mp3 + filename + ".mp3")
            print(f"{newmp3filename} is extracted successfully !!")

        if f"{filename}.pdf" not in listofeppdf:
            output_dir = f"{audioinpartsdirect + filename}/"
            part_size = 10
            audiofilepath = outputdirect_aud + newwavfilename
            split_wav(audiofilepath, output_dir, part_size)
            print("Audio file split into parts successfully")
            print(f"------------------------Working on {filename}.wav.../----------------------")

            audiototextbyparts(output_dir, newpdffilename)
        else:
            print(f"{filename}.pdf created already")

    print('----------------- All done--------------------')


def get_list_ofavalbland_notavalbl():
    pdf_path = base_path + "project1/app1/static/mypdffiles/"
    pdf_list = os.listdir(pdf_path)

    toteplist = getting_nd_beautifying_ep_namelist()
    available_eplist_sernums = get_allepnum_of3digit(pdf_path)
    # total_numofep_lst = [i for i in range(len(new_list))]
    available_eplist = [toteplist[a - 1] for a in range(len(toteplist)) if a in available_eplist_sernums]

    list1 = [[0, 1, 2] for a in range(len(toteplist))]
    for a_1 in range(len(toteplist)):
        # print(toteplist[a])
        for b in pdf_list:
            if str(a_1 + 1) in b and a_1 > 98:  # get_allepnum_of3digit() only work for 3 digit num epidode
                # print(a + 1)
                list1[a_1][0] = toteplist[a_1]
                list1[a_1][1] = b
                list1[a_1][2] = a_1

    for a_2, b, c in zip(list1, toteplist, range(len(list1) + 1)):
        if list1[c][0] == 0:
            list1[c][0] = toteplist[c]
            list1[c][1] = "NO pdf available"
            list1[c][2] = c

    return list1


"""def readhtmlpart1(path):
    file = open(path, "r", encoding='utf-8')
    part_1 = ""
    for html_linecode in file:
        part_1 += html_linecode
        if "<!-- part_1 end -->" in html_linecode:
            # print(html_linecode)
            break

    # print(part_1)
    file.close()

    return part_1


def readhtmlpart2(path):
    file = open(path, "r", encoding="UTF-8")
    part_2 = ""
    c = 0
    for html_linecode in file:
        if "<!-- part_2 start -->" in html_linecode:
            html_linecode = html_linecode.replace("</a></div><br>", "")
            # html_linecode = html_linecode.replace("</div><br>", "")
            # extra "</a></div><br>" is adding itslef after each time  don't know from where it is coming
            c += 1
        if c == 1:
            part_2 += html_linecode
        if html_linecode == "<!-- part_2 end -->":
            break

    # print(part_2)
    file.close()

    return part_2"""


def extract_line(start_phrase, end_phrase, full_sentence):
    # Find the index of the start phrase
    start_index = full_sentence.find(start_phrase)
    if start_index == -1:
        return "Start phrase not found"

    # Find the index of the end phrase
    end_index = full_sentence.find(end_phrase)
    if end_index == -1:
        return "End phrase not found"

    # Extract the line from the start phrase to the end phrase
    extracted_line = full_sentence[start_index:end_index + len(end_phrase)]

    return extracted_line.strip()


def readhtmlpart1(filepath):
    file_audiotoetxt = open(filepath, "r", encoding="UTF-8")
    htmlcode_2 = ""
    for html_linecode in file_audiotoetxt:
        htmlcode_2 += html_linecode
    file_audiotoetxt.close()

    start_phrase_2 = "<!-- part_1 start -->"
    end_phrase_2 = "<!-- part_1 end -->"
    full_sentence_2 = htmlcode_2

    part_1 = extract_line(start_phrase_2, end_phrase_2, full_sentence_2)

    return part_1


def readhtmlpart2(filepath):
    file_audiotoetxt = open(filepath, "r", encoding="UTF-8")
    htmlcode = ""
    for html_linecode in file_audiotoetxt:
        htmlcode += html_linecode
    file_audiotoetxt.close()

    start_phrase = "<!-- part_2 start -->"
    end_phrase = "<!-- part_2 end -->"
    full_sentence = htmlcode

    part_2 = extract_line(start_phrase, end_phrase, full_sentence)

    return part_2


def get_list_ofavalbland_notavalbl_2and_writing_and_savinghtml():
    listofaeps = get_list_ofavalbland_notavalbl()
    # print(listofaeps)
    path_to_audiohtml = base_path + "project1/app1/templates/gettextfromaudio.html"

    part_1 = readhtmlpart1(path_to_audiohtml)
    part_2 = readhtmlpart2(path_to_audiohtml)

    # Generate HTML code with <a> tags
    html_code = ''
    html_code += part_1
    for num in range(len(listofaeps)):
        if listofaeps[num][1] == "NO pdf available":
            html_code += f'<div class="notavailable" style="border-radius: 10px;"><a  target="pdfFrame"  href="#" >{listofaeps[num][0]}</a></div><br>'
        else:
            part1 = "{% static  '/mypdffiles/"
            part2 = "' %} "
            html_code += f'<div class="available" style="border-radius: 10px; "><a target="pdfFrame" href="{part1 + listofaeps[num][1] + part2}" target="_blank">{listofaeps[num][0]}</a></div><br>'
    html_code += part_2

    # Save or print the generated HTML code
    with open(
            base_path + 'project1/app1/templates/gettextfromaudio.html',
            'w', encoding='utf-8') as file:
        file.write(html_code)

    file.close()

    print("HTML code has been generated and saved to gettextfromaudio.html")


def getting_nd_beautifying_ep_namelist():
    ep_names_list = open(
        base_path + "project1/app1/mytextfiles/yakeplist.txt",
        "r")

    my_list = [ep_name for ep_name in ep_names_list]
    new_list = []

    for a in my_list:
        new_string = a.replace('â€¦', '-')
        new_string = new_string.replace('â€“', '-')
        new_string = new_string.replace("â€“", '-')
        new_list.append(new_string)
    return new_list


def read_html():
    file = open(base_path + "project1/app1/templates/"
                "gettextfromaudio.html", 'r', encoding='utf-8')
    for a in file:
        print(a.replace("\n", ""))
        # print(a)
    file.close()


# youtubehindi_link2text("https://youtu.be/bAARxYXOtSY?si=HhygVtFUQx92_lu9")
# dowload_video_andextractaudio("https://youtu.be/bAARxYXOtSY?si=HhygVtFUQx92_lu9")
def mk():
    # Assuming the file is UTF-8 encoded
    file_path = (base_path + "project1/app1/mytextfiles"
                 "/yakshincharacters.txt")
    my_list = []

    with open(file_path, 'r', encoding='utf-8') as FILE:
        for line in FILE:
            hindi_text = line.strip()
            my_list.append(hindi_text)
    FILE.close()

    return my_list


def getting_hineng_nameofchrs():
    s_2 = mk()
    list_5 = []
    nofchrs = 45
    for a2 in range(nofchrs):
        list_5.append(s_2[a2] + "/" + s_2[a2 + nofchrs])
    # print(list_5)
    part1 = '<img class="char_image" id="mainImage" src=\'{% static "/images/'
    part2 = '.jpeg" %}\' alt="My Image">'
    list_2 = []
    list_3 = []
    file = open(
        base_path + "project1/app1/mytextfiles/yakshincharacters.txt",
        "r", encoding='utf-8')
    c = 1
    numofchrs_2 = range(1, nofchrs + 1)
    for line_number, fileline in enumerate(file, start=1):
        if line_number in numofchrs_2:
            list_2.append(fileline)
            fileline = fileline.replace('\n', '')
            part1_new = part1.replace("mainImage", f"imageInput{line_number}")
            whole = part1_new + fileline + part2
            list_3.append(whole)
            c += 1
            print(whole)
    file.close()

    a = """
    <img id="mainImage" alt="Current Image">
<input type="file" accept="image/*" id="imageInput" style="display:none" onchange="chrimgprvw(this,'mainImage')">
<button onclick="openFileExplorer_tochoosenew_chrimg('imageInput')">Choose Image</button>
    """

    part_3 = """
    <div class= "grid-item">
    """
    part_4 = """
    <input type="file" accept="image/*" id="imageInput" style="display:none" onchange="chrimgprvw(this,"imageInput")">
    <button onclick="openFileExplorer_tochoosenew_chrimg()">Choose Image</button>
    <h3 style = "text-align: center;" >"""

    part_5 = """</h3>
    </div>"""

    for a in range(nofchrs):
        nm = "_id2"
        part_4_new = part_4.replace("id=\"imageInput\"", f"id=\"imageInput{str(a + 1) + nm}\"")
        part_4_new_1 = part_4_new.replace("chrimgprvw(this,\"imageInput\"",
                                          f"chrimgprvw(this,\'imageInput{a + 1}\'")
        id_name = f"\'imageInput{str(a + 1) + nm}\'"
        part_4_new_2 = part_4_new_1.replace("\"openFileExplorer_tochoosenew_chrimg()\"",
                                            f"\"openFileExplorer_tochoosenew_chrimg({id_name})\"")
        p = part_3 + list_3[a] + part_4_new_2
        p2 = p + list_5[a] + part_5
        print(p2)

    file = open(
        base_path + "project1/app1/mytextfiles"
        "/yakshincharacters.txt",
        "r", encoding='utf-8')
    c = 0
    for b in file:
        c += 1
        if c < nofchrs + 1:
            a = b.replace('\n', '')
            print(f"{a}.jpeg")
    file.close()


def load_immagelinkhtml():
    image_nameslist = os.listdir(
        base_path + "project1/app1/static/images")
    part1 = '<img class ="image" src="{% static \'/images/'
    part2 = '\' %}" alt="My Image" >'
    images_linklist = [part1 + a + part2 for a in image_nameslist]  # list comprehension
    return images_linklist


def imageLoaderHtml():
    path = base_path + "project1/app1/templates/lionimageloader.html"
    part_12 = readhtmlpart1(path)
    part_23 = readhtmlpart2(path)
    list2pathofimgs = os.listdir(
        base_path + "project1/app1/static/images")

    imagefile = open(path, 'w', encoding='utf-8')
    htmlcode = ""
    htmlcode += part_12
    part1 = '<img class ="image" src="{% static \'/images/'
    part2 = '\' %}" alt="My Image" >'
    for img in list2pathofimgs:
        newimageline = part1 + img + part2
        htmlcode += newimageline
        # print(part1 + img + part2)
    htmlcode += part_23

    imagefile.write(htmlcode)
    imagefile.close()

def download_video_yt_dlp(link, folder_path,video_name):
    try:
        ydl_opts = {
            # 'outtmpl': f'{folder_path}/%(title)s.%(ext)s',
            'outtmpl': folder_path + video_name ,
        }
        print(ydl_opts['outtmpl'])
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"Download completed! Video saved to {folder_path}")
    except Exception as e:
        print("An error occurred:", e)


