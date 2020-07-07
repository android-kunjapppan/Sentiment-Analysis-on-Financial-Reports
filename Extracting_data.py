import re
import Getting_files  

def extract_requried_data(data, section):
    mda_regex = re.finditer(r"item\s\d(.|[.])(|[.])\smanagement", data)
    qqdmr_regex = re.finditer(r"item\s\d(.|[.])(|[.])\squantitative", data)
    rf_regex = re.finditer(r"item\s\d(.|[.])(|[.])\srisk\sfactors", data)
    
    
    start_index = ending_index = 0
    counter = 1
    
    
    if section == "mda":
        for match in mda_regex:
            if counter == 1:
                ending_index = match.start()
            if counter == 2:
                start_index = match.start()
            counter += 1
    
    elif section == "qqdmr":
        for match in qqdmr_regex:
            if counter == 1:
                ending_index = match.start()
            if counter == 2:
                start_index = match.start()
            counter += 1
            
    elif section == "rf":
        for match in rf_regex:
            if counter == 1:
                ending_index = match.start()
            if counter == 2:
                start_index = match.start()
            counter += 1
            
    end_content = data[ending_index : ending_index + 500]
    item_ = re.finditer(r"item\s\d([.]|.)", end_content)
    counter = 1
    start_value = end_value = 0
    
    
    for match in item_:
        if counter == 2:
            start_value = match.start()
            end_value = match.end()
        counter += 1
        
    end_section = end_content[start_value:end_value]

    data = data[start_index::]
    
    end_regex = re.finditer(r"{}".format(end_section), data)
    end_section_index = 0
    
    for match in end_regex:
        end_section_index = match.start()
        break

    return data[:end_section_index]


total_links = len(Getting_files.urls) + 1


for i in range(1, total_links):
    f = open("sec_{}.txt".format(i), "r",encoding="utf8")
    string = f.read()
    
    temp = re.sub("[^a-zA-Z0-9'., ]", " ", string)
    
    temp = " ".join(temp.split())
   
    consequitivedots = re.compile(r"\.{3,}")
    temp = consequitivedots.sub("", temp)
    
    data = temp.lower()
    
    
    mda_content = extract_requried_data(data, "mda")
    qqdmr_content = extract_requried_data(data, "qqdmr")
    rf_content = extract_requried_data(data, "rf")
    
    file2write_mda = open("file_mda_{}.txt".format(i), "w+", encoding="UTF-8")
    file2write_mda.write(mda_content)
    file2write_mda.close()
    file2write_qqdmr = open("file_qqdmr_{}.txt".format(i), "w+", encoding="UTF-8")
    file2write_qqdmr.write(qqdmr_content)
    file2write_qqdmr.close()
    file2write_rf = open("file_rf_{}.txt".format(i), "w+", encoding="UTF-8")
    file2write_rf.write(rf_content)
    file2write_rf.close()
    
            

