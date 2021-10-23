import pytube
import sys

def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining) / stream.filesize)
    percent = ('{0:.1f}').format(current * 100)
    progress = int(50 * current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write('  |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()


def download(url, d_dir=None):
    youtube = pytube.YouTube(url)
    youtube.register_on_progress_callback(progress_function)
    video = youtube.streams.get_highest_resolution()  # loading video highest quality.
    print("--------------------")
    print("Title : " + video.title)
    print("--------------------")
    if d_dir is not None:
        video.download(d_dir)
    else:
        video.download()

    print("Download completed!")


if __name__ == '__main__':
    url = input("URL:")
    d_dir = input("Specify the download directory(Leave blank if you haven't decided.):")

    download(url, d_dir)
