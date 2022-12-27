# this is youtube downloader
import os,sys
from pytube import YouTube
from datetime import datetime
import time

now = datetime.now()

def mp3_download():
	print("""\033[0;34m
		       t          L
            ..       : ED.        #K:
           ,W,     .Et E#K:       :K#t
          t##,    ,W#t E##W;        L#G.
         L###,   j###t E#E##t        t#W, 
       .E#j##,  G#fE#t E#ti##f    .jffD##f
      ;WW; ##,:K#i E#t E#t ;##D. .fLLLD##L
     j#E.  ##f#W,  E#t E#ELLE##K:    ;W#i 
   .D#L    ###K:   E#t E#L;;;;;;,   j#E.
  :K#t     ##D.    E#t E#t        .D#f
  ...      #G      ..  E#t        KW,
           j                      G.\033[0m""")
	print(now)

	link = input('\033[0;36mPaste your link here to download mp3: \033[0m')
	
	try:
		YtO = YouTube(link)
		audio = YtO.streams.filter(only_audio=True).first()
		destionation = input('enter your destionation >>> ') or '.'
		out_file = audio.download(output_path=destionation)


		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)



	except:
		print("\033[0;31mError to downloading audio!\033[0m")
		
	print("\033[0;32mAudio download completed!\033[0m")
    


def Download():
	print("""\033[0;34m
	     ;
             ED.
             E#Wi
             E###G.               i
             E#fD#W;             LE
  t      .DD.E#t t##L           L#E
  EK:   ,WK. E#t  .E#K,        G#W.
  E#t  i#D   E#t    j##f      D#K.
  E#t j#f    E#t    :E#K:    E#K.
  E#tL#i     E#t   t##L    .E#E.
  E#WW,      E#t .D#W;    .K#E
  E#K:       E#tiW#G.    .K#D
  ED.        E#K##i     .W#G
  t          E##D.     :W##########Wt 
             E#t       :,,,,,,,,,,,,,.
             L:\033[0m""")
	print(now)

	link = input('\033[0;36mPaste your link here to download video: \033[0m')
	YtO = YouTube(link)
	YtO = YtO.streams.get_highest_resolution()
	try:
		YtO.download()
	except:
		print ("\033[0;31m Error to downloading your youtube video\033[0m")
	  
	print ("\033[0;31m Video download completed!\033[0m")
    



def main():
	global option
	os.system('cls')
	print("""\033[0;34m
                       ;
                       ED.
                       E#Wi
                       E###G.               i
  f.     ;WE. GEEEEEEELE#fD#W;             LE
  E#,   i#G   ,;;L#K;;.E#t t##L           L#E
  E#t  f#f       t#E   E#t  .E#K,        G#W.
  E#t G#i        t#E   E#t    j##f      D#K.
  E#jEW,         t#E   E#t    :E#K:    E#K.
  E##E.          t#E   E#t   t##L    .E#E.
  E#G            t#E   E#t .D#W;    .K#E
  E#t            t#E   E#tiW#G.    .K#D
  E#t            t#E   E#K##i     .W#G
  EE.             fE   E##D.     :W##########Wt 
  t                :   E#t       :,,,,,,,,,,,,,.
                       L:\033[0m""")
	print(now)

	print ("\033[0;35m\nPlease choose your option above!\n\033[0m")
	print ("\033[0;36m[YTD]   : For youtube download.\033[0m")
	print ("\033[0;36m[mp3dl] : For mp3 youtube download.\033[0m")
	option = str(input('\033[0;32m\nEnter your option: \033[0m'))

	if option == 'YTD':
		os.system('cls')
		Download()
	elif option == 'mp3dl':
		os.system('cls')
		mp3_download()
	else:
		print (str("\033[0;31mError: "+ option))
		time.sleep(3)

main()

