function optional_flag(){

for OPT in "$@"
do
    case $OPT in
        -a)
            FLAG_A=1
            ;;
        -b)
            FLAG_B=1
            VALUE_B=$2
            shift
            ;;
    esac
    shift
done

if [ "$FLAG_A" ]; then
    echo "Option -a specified."
fi

if [ "$FLAG_B" ]; then
    echo "Option -b $VALUE_B specified."
fi
}
optional_flag $@
