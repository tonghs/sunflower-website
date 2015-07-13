while true
do
    python /home/tonghs/sunflower-website/app.py

    for i in $(seq 5)
    do
        echo $i
        sleep 1
    done

done
