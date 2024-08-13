import csv
import os
from pathlib import Path
from turtledemo.minimal_hanoi import play
from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
from pytube import YouTube
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import requests
from bs4 import BeautifulSoup


# from testProjects.mypyfiles.audiototext import createfilename

def get_files_sorted_by_date(folder_path="."):
    folder_path = Path(folder_path)

    # Get all files in the specified directory
    files = [f for f in folder_path.iterdir() if f.is_file()]

    # Sort files by creation time
    files_sorted_by_date = sorted(files, key=lambda f: f.stat().st_ctime)

    return files_sorted_by_date
    """
    # Example usage:
folder_path = "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/Excelfiles"
sorted_files = get_files_sorted_by_date(folder_path)

for file in sorted_files:
    print(f"{file.name} - Created on: {file.stat().st_ctime}")
    """


def extractapname(filename="yakepsname1to814.txt"):
    epdetailfile = open(filename, "r")
    epnamefile = open("yakeplist.txt", "a")
    for fileline in epdetailfile:
        if fileline[:2] == "Ep":
            # epnamefile.write(fileline)
            print(fileline)
    print("check the files : ")
    epnamefile.close()
    epdetailfile.close()

    # new modification's
    num = ""
    numlist = []
    # yt = YouTube(link)
    # orgvidnm = yt.title
    # orgvidnm = removespace(word=orgvidnm)
    # video_length = yt.length

    """for a in orgvidnm:
        if a.isnumeric():
            if len(num) < 3:
                num += a
                if len(num) == 3:
                    numlist.append(num)
                    num = ""

    epnumlist = sorted(list(set(numlist)))"""


# example usage:

"""def download_youtube_video(url, save_path):
    try:
        # Create a YouTube object for the given URL
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        new_name = createfilename(yt.title) + ".mp4"
        save_file_path = os.path.join(save_path, new_name)
        stream.download(output_path=save_path, filename=new_name)
        print(f"Video '{new_name}' downloaded and saved to '{save_file_path}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")"""


def pdfmaker(filename, paragraph, ap=None):
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment(paragraph)

    page.paragraphs.add(text_fragment)

    document.save(
        'C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/static/mypdffiles/' + filename + '.pdf')  # Save updated PDF
    print(
        '----------------------------------------------------pdf created succesefully---------------------------------------------')


def pdfmaker_2(filename, paragraph):
    output_file = "output.pdf"
    c = canvas.Canvas(
        'C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mypdffiles/' + filename + '.pdf',
        pagesize=letter)
    font_size = 10
    c.setFont("Helvetica", font_size)
    c.drawString(100, 500, paragraph)
    c.save()
    print(f"PDF created and saved as '{output_file}'")


def extract_audio_from_video(video_path, output_audio_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_audio_path, codec='pcm_s16le')
        print(f"Audio extracted and saved as {output_audio_path} in WAV format")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def playwav(audiopath):
    wav_file = AudioSegment.from_file(file=audiopath, format="wav")
    play(wav_file)


# 12:17 PM 8/13/2023
def paragraph_maker(single_line, wrdsperln=40):
    # taking the input for the number of words per line
    # words prt line
    # wrdsperln  = int(input("Enter width of paragraph (width is number of Words per line >>)"))
    words = single_line.split(' ')  # list of all words in the bigger line
    paragraph = []
    sentence = ''
    number_of_line = len(words) // wrdsperln
    sn = 0

    for a in range(number_of_line):
        for a in range(sn, wrdsperln + sn):  # sn - starting index for new line
            sentence += ' ' + words[a]
        sn = sn + wrdsperln
        paragraph.append(sentence)
        sentence = ''

    nbrofwrdsinlstln = len(words) % wrdsperln  # number of words in last line
    lstlnstrtind = len(words) - nbrofwrdsinlstln + 1  # last_line_starting_index
    sentence = ''
    for a in range(nbrofwrdsinlstln - 1):
        sentence += ' ' + words[lstlnstrtind]
        lstlnstrtind += 1
    paragraph.append(sentence)

    for a in paragraph:
        return a


"""def checkfilename(link):
    try:
        yt = YouTube(link)
        videoname = yt.title
        videoname = createfilename(link) + '.mp4'
        file_name = "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/videosdirect/" + videoname
        video_length = yt.length
        print(file_name)
        if os.path.isfile(file_name):
            return 0
        else:
            print("File is not present , we are downloading it now ")
    except:
        print("check code ! something is missed Be Calm and find it !! Khojo ")"""


def get_episodes_titles(link):
    num = ""
    numlist = []
    yt = YouTube(link)
    orgvidnm = yt.title
    video_length = yt.length
    for a in orgvidnm:
        if a.isnumeric():
            if len(num) < 3:
                num += a
                if len(num) == 3:
                    numlist.append(num)
                    num = ""
    epnumlist = sorted(list(set(numlist)))

    ep_num = []
    ep_names_list = open(
        "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mytextfiles/yakeplist.txt", "r")
    for fileline in ep_names_list:
        if fileline[3:6] in epnumlist:
            # print(fileline)
            a = int(epnumlist[0])
            z = int(epnumlist[-1])
            # print(a,z)
            while a < z + 1:
                # print(a, z)
                ep_num.append(str(a))
                a += 1
            break
    ep_names_list.close()

    ep_names_list_modified = []
    ep_names_list = open(
        "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mytextfiles/yakeplist.txt", "r")
    for fileline in ep_names_list:
        # print(fileline)
        if fileline[3:6] in ep_num:
            # print(fileline[3:6])
            ep_names_list_modified.append(fileline)
    # print(ep_names_list_modified)
    ep_names_list.close()

    return ep_names_list_modified


def load_ep_names():
    ep_names_list = open(
        "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mytextfiles/yakeplist.txt", "r")
    my_list = [ep_name for ep_name in ep_names_list]
    return my_list


def print_something():
    print('here is written something')


def getting_linkTopdf():
    part1 = "{% static  '/mypdffiles/"
    part2 = "' %/\""
    pdf_list = os.listdir("C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mypdffiles")
    linkTopdf = [part1 + a + part2 for a in pdf_list]
    return linkTopdf


# 10:27 PM 8/12/2023
def audiototext(path_to_audfile, aai=None):
    aai.settings.api_key = "83c391aaebc4499e942322e6e431bdd8"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe(path_to_audfile)
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")

    print(transcript.text)


def setlinkandepname(link):
    path = "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mytextfiles/linklisttext.txt"
    linkfile = open('path', 'a')
    linkfile.writelines(link, YouTube.title)


def mk():
    # Assuming the file is UTF-8 encoded
    file_path = ("C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mytextfiles"
                 "/yakshincharacters.txt")
    my_list = []

    with open(file_path, 'r', encoding='utf-8') as FILE:
        for line in FILE:
            hindi_text = line.strip()
            my_list.append(hindi_text)

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
        "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mytextfiles/yakshincharacters.txt",
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
        "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mytextfiles"
        "/yakshincharacters.txt",
        "r", encoding='utf-8')
    c = 0
    for b in file:
        c += 1
        if c < nofchrs + 1:
            a = b.replace('\n', '')
            print(f"{a}.jpeg")
    file.close()


# getting_hineng_nameofchrs()

# https://youtu.be/Oez0echaN-c?si=XdKZS0qPXNioepJb,https://youtu.be/UAaUqTwN_7E?si=yySou16IiYR-BpmJ,https://youtu.be/m0Sid-TyQa0?si=RfEZE0dsmoFKGVnf,https://youtu.be/fY3WCn9_EcQ?si=-Z0StFPdoi_9cgct,https://youtu.be/QZg-8OYxwOs?si=sWDMjuQhrxJRlU6Z,https://youtu.be/VBS6dy8DTLU?si=c-q0RF4mltNfg2au


def load_immagelinkhtml():
    image_nameslist = os.listdir(
        "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/static/images")
    part01 = '<img class ="image" src="{% static \'/images/'
    part02 = '\' %}" alt="My Image" >'
    images_linklist = [part01 + a2 + part02 for a2 in image_nameslist]  # list comprehension
    return images_linklist


def get_text_from_web():
    # URL of the website to scrape
    url = 'https://www.pocketfm.com/show/3842a3903bff3cd0f475f178701bbc9879fe6ba6/all-episodes'

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and extract the text content
        text_content = soup.get_text()

        # Print the extracted text
        print(text_content)
    else:
        print('Failed to fetch data from the website:', response.status_code)


# get_text_from_web()


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


def imageLoaderHtml():
    path = "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/templates/lionimageloader.html"
    part_12 = readhtmlpart1(path)
    part_23 = readhtmlpart2(path)
    print(part_23)

    list2pathofimgs = os.listdir(
        "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/static/images")
    imagefile = open(path, 'w', encoding='utf-8')
    htmlcode = ""

    htmlcode += part_12

    part1 = '<img class ="image" src="{% static \'/images/'
    part2 = '\' %}" alt="My Image" >'
    for img in list2pathofimgs:
        htmlcode += part1 + img + part2

    htmlcode += part_23

    imagefile.write(htmlcode)
    imagefile.close()


# imageLoaderHtml()

"""
filepath = "C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/templates/lionimageloader.html"
file = open(filepath, "r", encoding="UTF-8")
htmlcode = ""
for htmlline in file:
    htmlcode += htmlline

file.close()"""


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


# imageLoaderHtml()

def convert_text_to_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    records = []
    i = 0
    while i < len(lines):
        name = lines[i].strip()
        status = lines[i + 1].strip()
        party = lines[i + 2].strip()
        # Skipping two lines
        district_state = lines[i + 4].strip().split(" | ")
        district = district_state[0]

        state = district_state[1]
        # print(name, status, party, district, state)
        records.append([name, status, party, district, state])
        # Move to the next record
        i += 7
    print(records)
    print(len(records))

    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Name', 'Status', 'Party', 'District', 'State'])
        csvwriter.writerows(records)
    """
    # Example usage
input_file = 'C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mytextfiles/2024wincandidates.txt'
output_file = 'C:/Users/dell pc/PycharmProjects/pythonProject1/djangoProjects/project1/app1/mytextfiles/records.csv'
convert_text_to_csv(input_file, output_file)"""


"""
import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
for package in packages:
    call(f"pip install --upgrade {package}", shell=True)

"""