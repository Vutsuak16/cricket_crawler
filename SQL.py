__author__ = 'kasutuv'
import MySQLdb

def insert_db(data):
    try:
        conn = db = MySQLdb.connect("localhost","root","","cricket_crawler" )
        cur = conn.cursor()
        data1,s,country,data2=modify(data)
        print data
        print s
        cur.execute(
            "CREATE  TABLE IF NOT EXISTS cric_players(pname varchar(20) DEFAULT 'N.A.',pfullname varchar(40) NOT NULL,pcountry VARCHAR(20)DEFAULT 'N.A.',pborn varchar(60) DEFAULT 'N.A.',pcage varchar(20) DEFAULT 'N.A.',pmteam varchar(150) DEFAULT 'N.A.',pnick varchar(15) DEFAULT 'N.A.',prole varchar(25) DEFAULT 'N.A.',pbatt varchar(25) DEFAULT 'N.A.',pbowl varchar(25) DEFAULT 'N.A.' ,pfield varchar(25) DEFAULT 'N.A.',pprofile VARCHAR(1000) DEFAULT 'N.A.',PRIMARY KEY(pfullname));")
        if len(data1) is 10:
            cur.execute(
                "INSERT INTO cric_players(pname, pfullname , pborn, pcage, pmteam ,pnick ,prole ,pbatt ,pbowl, pfield) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data1)
        elif len(data1) is 9:
            cur.execute(
                "INSERT INTO cric_players(pname, pfullname, pborn, pcage, pmteam, prole, pbatt, pbowl, pfield) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", data1)
        elif len(data1) is 8:
            cur.execute(
                "INSERT INTO cric_players(pname, pfullname, pborn, pcage, pmteam ,prole ,pbatt ,pbowl) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", data1)
        elif len(data1) is 7:
            cur.execute(
                "INSERT INTO cric_players(pname, pfullname, pborn, pcage, pmteam ,pbatt ,pbowl) VALUES(%s,%s,%s,%s,%s,%s,%s)", data1)
        cur.execute(
            "UPDATE cric_players SET pmteam =%s WHERE pfullname =%s ", [s[:-1],data1[1]])
        cur.execute(
            "UPDATE cric_players SET pprofile =%s WHERE pfullname =%s ",[data2[1:],data1[1]])
        cur.execute(
            "UPDATE cric_players SET pcountry =%s WHERE pfullname =%s ", [country[:-1],data1[1]])
        conn.commit()
        cur.close()
        conn.close()

    except MySQLdb.Error, e:
        print "Mysql Error 1 "
def showall_db(**args):
    try:
        conn = db = MySQLdb.connect("localhost","root","","cricket_crawler" )
        cur = conn.cursor()
        flag=1
        if not args:
            cur.execute("SELECT * FROM cric_players")
        if args.get("arg1")=="pname" and args.get("arg2"):
            cur.execute("SELECT * FROM cric_players WHERE pname LIKE %s  ",[args.get("arg2")])
        if args.get("arg1")=="pcountry" and args.get("arg2"):
            cur.execute("SELECT * FROM cric_players WHERE pcountry LIKE %s  ",[args.get("arg2")])
        if args.get("arg1")=="pbatt" and args.get("arg2"):
            cur.execute("SELECT * FROM cric_players WHERE pbatt LIKE %s  ",[args.get("arg2")])
        if args.get("arg1")=="prole" and args.get("arg2"):
            cur.execute("SELECT * FROM cric_players WHERE prole LIKE %s  ",[args.get("arg2")])
        if args.get("arg1")=="pbowl" and args.get("arg2"):
            cur.execute("SELECT * FROM cric_players WHERE pbowl LIKE %s  ",[args.get("arg2")])
        if args.get("arg1")=="pfield" and args.get("arg2"):
            cur.execute("SELECT * FROM cric_players WHERE pfield LIKE %s  ",[args.get("arg2")])
        results = cur.fetchall()

        try:
            results[0]
        except:
            return "Data not Found"
        disp=""
        for row in results:
            pname=row[0]
            pfullname=row[1]
            pcountry=row[2]
            pborn=row[3]
            pcage=row[4]
            pmteam=row[5]
            pnick=row[6]
            prole=row[7]
            pbatt=row[8]
            pbowl=row[9]
            pfield=row[10]
            pprofile=row[11]


            if not args.get("arg3") or args.get("arg3")=="All Info":
                print "Player Name = %s Fullname = %s, Country = %s, Born on = %s, CurrentAge = %s, MajorTeam = %s, Nick = %s, Role = %s, Batting = %s, Bowling = %s, Field = %s,\n Profile = %s" %(pname, pfullname, pcountry, pborn, pcage, pmteam, pnick, prole, pbatt, pbowl, pfield, pprofile)
                disp=disp+"Player Name = "+ pname +"\nFullname = "+pfullname+",\nCountry = "+pcountry+",\nBorn on = "+pborn+",\nCurrentAge = "+pcage+",\nMajorTeam = "+pmteam+",\nNick = "+pnick+",\nRole = "+prole+",\nBatting = "+pbatt+",\nBowling = "+pbowl+", Field = "+pfield+",\n Profile = "+ pprofile
            if args.get("arg3")=="Player Name":
                print "Player Name = %s"%pname
                disp=disp+"Player Name = "+ pname+"\n"
            if args.get("arg3")=="Country":
                print "Player Country = %s"%pcountry
                disp=disp+"Player Country = "+pcountry+"\n"
            if args.get("arg3")=="Born":
                print "Born = %s"%pborn
                disp=disp+"Born = "+pborn+"\n"
            if args.get("arg3")=="Current Age":
                print "Current Age = %s"%pcage
                disp=disp+"Current Age = "+pcage+"\n"
            if args.get("arg3")=="Major Teams":
                print "Played For = %s"%pmteam
                disp=disp+"Played For = "+pmteam+"\n"
            if args.get("arg3")=="Profile":
                print "Player Profile = %s"%pprofile
                disp=disp+"Player Profile = "+pprofile+"\n"


        conn.commit()
        cur.close()
        conn.close()
        return disp




    except MySQLdb.Error, e:
        print "Mysql Error 2"
        return 0



def modify(data):
    data2=data.pop(-1)
    s=""
    for i in range(len(data2)):
        if(data2[i] in [',','.']):
            s=s+"\n"
        else:
            s=s+data2[i]
    data2=s
    data1,s,country=modify2(data)
    return data1,s,country,data2

def modify2(data):
    s=""
    country=""
    flag=0
    for word in data[:]:
        if word.endswith(','):
            s=s+word
            if not flag:
                country=country+word
                flag=1
            data.remove(word)
        if word is '':
            data.remove(word)
    return data,s,country