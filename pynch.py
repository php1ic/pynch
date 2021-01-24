import datetime
import nubase_parse

if __name__ == '__main__':
    datafile = r"/home/ijc/Nuclear_chart/Draw_chart/inch/data_files/nubtab03.asc"

    data = nubase_parse.NubaseParser(datafile, 2003)
    print(datetime.datetime.now())
    df = data.read_file()
    print(datetime.datetime.now())
    print(df)
