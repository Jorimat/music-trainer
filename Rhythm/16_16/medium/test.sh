while getopts b: option
do
case "${option}"
in
b) BARS=${OPTARG};;
esac
done    

echo $BARS


python3 test.py -b $BARS