rm -rf mp4
mkdir mp4
for i in *.GIF; do ffmpeg -i $i -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" "./mp4/${i%.*}.mp4"; done     
#for i in *.GIF; do ffmpeg -i $i -movflags faststart -pix_fmt yuv420p -vf "scale=300:180:" "./mp4/enroll_1_${i%.*}.mp4"; done     
