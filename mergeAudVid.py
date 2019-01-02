import os


def extractaudio(filename):

    os.system("""ffmpeg -i """+filename+""" -nostats -loglevel 0 -vn -acodec copy """+filename+""".aac""")
    return str(filename+".aac")


def mutevideo(filename):

    # print("Entered Mute Video")
    mutedfilename = filename[:len(filename)-4]+".muted"+filename[len(filename)-4:]
    os.system("""ffmpeg -i """+filename+""" -nostats -loglevel 0 -codec copy -an """+mutedfilename)
    return mutedfilename



def mergevideoaudio(filename, mutevid):

    os.system("""ffmpeg -i """+mutevid+""" -nostats -loglevel 0 -i output.aac -shortest -c:v copy -c:a aac -b:a 256k -strict -2 """+filename+""".output.mp4""")
