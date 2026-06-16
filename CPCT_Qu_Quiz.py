import streamlit as st

# Page configuration for mobile view
st.set_page_config(page_title="ANEESH MAKE CPCT QUIZ", page_icon="🎓", layout="centered")

# --- 1. NEON GOLD GLOW CSS FOR LOGIN & GAME ---
design_css = """
<style>
    .stApp { 
        background: radial-gradient(circle, #1a1a1a 0%, #0d0d0d 100%);
        color: #ffffff;
    }
    .main-card {
        background: #1f1f1f;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 0px 25px rgba(197, 160, 89, 0.6);
        border: 2px solid #c5a059;
        text-align: center;
        margin-bottom: 20px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { box-shadow: 0 0 15px rgba(197, 160, 89, 0.4); }
        to { box-shadow: 0 0 30px rgba(255, 215, 0, 0.8); }
    }
    .header-text { 
        color: #ffd700; 
        font-family: 'Georgia', serif; 
        font-size: 32px; 
        font-weight: bold;
        text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    .gold-line { 
        height: 2px; 
        background: linear-gradient(to right, transparent, #ffd700, transparent); 
        margin: 15px 0; 
    }
    .section-badge {
        background-color: #c5a059;
        color: #000000;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 10px;
    }
    .question-box {
        background-color: #262626;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ffd700;
        margin-bottom: 20px;
        font-size: 18px;
        line-height: 1.6;
    }
    .hindi-text {
        color: #e0e0e0;
        font-size: 16px;
        margin-top: 10px;
        border-top: 1px dashed #555;
        padding-top: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #2b2b2b !important;
        color: white !important;
        border: 1px solid #c5a059 !important;
    }
    .stButton>button {
        width: 100% !important;
        background-color: #2a2a2a !important;
        color: #ffd700 !important;
        border: 1px solid #c5a059 !important;
        font-weight: bold !important;
        padding: 10px !important;
    }
    .stButton>button:hover {
        background-color: #ffd700 !important;
        color: #000000 !important;
        box-shadow: 0 0 15px #ffd700;
    }
</style>
"""
st.markdown(design_css, unsafe_allow_html=True)

# --- 2. FULL 75 QUESTIONS DATA BANK ---
quiz_data = []

# --- COMPUTER PROFICIENCY SECTION (Q1 to Q25) ---
sect = "Computer Proficiency & IT Skills"

quiz_data.append({"section": sect, "q_eng": "Cache and main memory will lose their contents when the power of a computer is off. This property is referred to as ____________.", "q_hin": "कैश और मुख्य मेमोरी अपनी सामग्री खो देंगे जब बिजली बंद हो जाएगी, इस गुण को ____________ कहा जाता है।", "options": ["Dynamic", "Static", "Volatility", "Non-volatile"], "answer": "Volatility"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is a set of instructions embedded on a piece of hardware at the time of manufacturing and tells the device how to operate?", "q_hin": "निम्नलिखित में से कौन सा हार्डवेयर के निर्माण के समय उस पर सन्निहित निर्देशों का एक सेट है और डिवाइस को संचालित करने का तरीका बताता है?", "options": ["Application Software", "Utility Software", "Firmware", "Freeware"], "answer": "Firmware"})

quiz_data.append({"section": sect, "q_eng": "____________ is a programmable device that takes in input, performs some arithmetic and logical operations over it and produces the desired output.", "q_hin": "____________ एक प्रोग्राम करने योग्य डिवाइस है जो इनपुट लेता है, उस पर कुछ अंकगणितीय और तार्किक ऑपरेशन करता है और वांछित आउटपुट उत्पन्न करता है।", "options": ["SMPS", "UPS", "Microprocessor", "Bus"], "answer": "Microprocessor"})

quiz_data.append({"section": sect, "q_eng": "You CANNOT save an MS-Excel 2016 file in a/an ____________ format.", "q_hin": "आप MS-Excel 2016 फाइल को ____________ फ़ॉर्मेट में सेव नहीं कर सकते।", "options": ["PDF", "PSD", "TXT", "XML"], "answer": "PSD"})

quiz_data.append({"section": sect, "q_eng": "What does the term SCSI stand for?", "q_hin": "SCSI का पूर्ण रूप ____________ है।", "options": ["Small Computer Software Interface", "Small Computer Storage Interface", "Small Computer System Interface", "Small Computer Standard Interface"], "answer": "Small Computer System Interface"})


quiz_data.append({"section": sect, "q_eng": "The most common input devices are:", "q_hin": "इनमे से सबसे आम इनपुट डिवाइस कौन-सी हैं?", "options": ["Microphone and Printer", "Scanner and Monitor", "Digital Camera and Speaker", "Keyboard and Mouse"], "answer": "Keyboard and Mouse"})

quiz_data.append({"section": sect, "q_eng": "In a computer, which device is functionally opposite to a keyboard?", "q_hin": "एक कंप्यूटर में, कौन-सा डिवाइस कार्यात्मक रूप से कीबोर्ड से विपरीत है?", "options": ["Joystick", "Track ball", "Mouse", "Printer"], "answer": "Printer"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is Python language editor?", "q_hin": "इनमें से कौन पायथन भाषा संपादक है?", "options": ["Tally", "Coda", "Jupyter", "SnapTouch"], "answer": "Jupyter"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is utility software?", "q_hin": "निम्नलिखित में से कौनसा यूटिलिटी सॉफ्टवेयर है?", "options": ["Avast Antivirus", "BIOS", "Android", "MS-Word"], "answer": "Avast Antivirus"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is true with reference to DVD?", "q_hin": "DVD के संदर्भ में निम्नलिखित में से कौन सा सत्य है?", "options": ["Full form of DVD is Digital Valid Disk.", "DVDs are not portable.", "DVD-R offers a write once approach.", "DVD ROM is used for both reading and writing."], "answer": "DVD-R offers a write once approach."})

quiz_data.append({"section": sect, "q_eng": "Which of the following is an example of open source software?", "q_hin": "निम्नलिखित में से कौन सा ओपन सोर्स सॉफ्टवेयर का एक उदाहरण है?", "options": ["Netflix", "MySQL", "McAfee", "Google Chrome"], "answer": "MySQL"})

quiz_data.append({"section": sect, "q_eng": "Which of the following plotters draws exact vector graphics on paper or other media?", "q_hin": "निम्नलिखित में से कौन सा प्लॉटर कागज़ या अन्य मीडिया पर सटीक वेक्टर ग्राफ़िक्स बनाता है?", "options": ["Cutting Plotter", "Pinch Roller", "Cycle Plotter", "Drum Plotter"], "answer": "Drum Plotter"})

quiz_data.append({"section": sect, "q_eng": "____________ is an internet service consisting of thousands of newsgroups.", "q_hin": "____________ एक इंटरनेट सेवा है जिसमें हजारों समाचार समूह शामिल हैं।", "options": ["USECASE", "USENET", "USESET", "UCENET"], "answer": "USENET"})

quiz_data.append({"section": sect, "q_eng": "Which of the following keyboard shortcut keys is used to rename a highlighted icon, file or folder in Windows 10?", "q_hin": "Windows 10 में हाइलाइट किए गए आइकन, फाइल या फोल्डर का नाम बदलने के लिए निम्न में से किस कीबोर्ड शॉर्टकट कुंजी का उपयोग किया जाता है?", "options": ["F3", "F5", "F2", "F4"], "answer": "F2"})

quiz_data.append({"section": sect, "q_eng": "Cortana is an intelligent personal assistant developed by ____________.", "q_hin": "कॉर्टाना ____________ द्वारा विकसित एक बुद्धिमान व्यक्तिगत सहायक है।", "options": ["Microsoft", "Apple", "HP", "Oracle"], "answer": "Microsoft"})

quiz_data.append({"section": sect, "q_eng": "Which of the following devices is commonly used to protect an internal network from unwanted access?", "q_hin": "अवांछित पहुंच से आंतरिक नेटवर्क की सुरक्षा के लिए आमतौर पर कौन-सा डिवाइस उपयोग किया जाता है?", "options": ["Firewall", "Router", "Switch", "Hub"], "answer": "Firewall"})

quiz_data.append({"section": sect, "q_eng": "Which of the following statements is/are true? (i) GUI actions are through direct manipulation. (ii) Dialogue box asks for input.", "q_hin": "निम्नलिखित में से कौन-सा कथन सत्य है? (i) GUI में क्रियाएं सीधे हेरफेर से होती हैं। (ii) डायलॉग बॉक्स इनपुट मांगता है।", "options": ["Only (i)", "Only (ii)", "Both (i) and (ii)", "Neither (i) nor (ii)"], "answer": "Both (i) and (ii)"})

quiz_data.append({"section": sect, "q_eng": "A grey scale picture in JPEG is divided into blocks of ____________ pixels.", "q_hin": "JPEG में एक ग्रे स्केल चित्र, ____________ पिक्सल के ब्लॉक में विभाजित होती है।", "options": ["6x6", "5x5", "7x7", "8x8"], "answer": "8x8"})

quiz_data.append({"section": sect, "q_eng": "Which of the following ranges across countries and continents? (i) LAN (ii) MAN (iii) WAN", "q_hin": "निम्नलिखित में से किसकी रेंज देश और महाद्वीपों तक होती है? (i) LAN (ii) MAN (iii) WAN", "options": ["Only (i)", "Only (ii)", "Only (iii)", "Both (i) and (ii)"], "answer": "Only (iii)"})

quiz_data.append({"section": sect, "q_eng": "The security property which defines the ability of a system to ensure that an asset is modified only by authorised parties is called ____________.", "q_hin": "सुरक्षा संपत्ति जो यह सुनिश्चित करती है कि एक संपत्ति केवल अधिकृत पार्टियों द्वारा संशोधित की जाती है, उसे ____________ कहा जाता है।", "options": ["Availability", "Confidentiality", "Integrity", "Cryptograph"], "answer": "Integrity"})

quiz_data.append({"section": sect, "q_eng": "How to view the MAC address associated with Windows 10 Ethernet device?", "q_hin": "Windows 10 ईथरनेट डिवाइस से जुड़े MAC पते को कैसे देखें?", "options": ["Settings->Network and Internet->Status->Properties", "Settings->Dial-up->Properties", "Settings->VPN->Properties", "Settings->Proxy->Properties"], "answer": "Settings->Network and Internet->Status->Properties"})

quiz_data.append({"section": sect, "q_eng": "AES symmetric encryption algorithm performs all its computations on ____________ of data rather than in bits.", "q_hin": "AES सममित एन्क्रिप्शन एल्गोरिथ्म बिट्स के बजाय डेटा के ____________ पर अपनी सभी गणना करता है।", "options": ["Bytes", "Numbers", "Cells", "Digits"], "answer": "Bytes"})

quiz_data.append({"section": sect, "q_eng": "When a router needs to send a packet to another computer/network, then it should know which of the following?", "q_hin": "जब किसी राउटर को एक पैकेट को दूसरे कंप्यूटर नेटवर्क में भेजना होता है, तो उसे क्या पता होना चाहिए?", "options": ["Datagram", "Path name", "Transport medium", "IP address"], "answer": "IP address"})

quiz_data.append({"section": sect, "q_eng": "How is the computer monitor size measured?", "q_hin": "मॉनिटर का आकार कैसे मापा जाता है?", "options": ["From left top to left bottom", "From right top to right bottom", "From corner to corner diagonally", "From left top to right top"], "answer": "From corner to corner diagonally"})

quiz_data.append({"section": sect, "q_eng": "A/an ____________ is a weakness in an information system, system security procedures, or internal controls that could be exploited by a threat source.", "q_hin": "____________ एक सूचना प्रणाली, सिस्टम सुरक्षा प्रक्रियाओं या आंतरिक नियंत्रण में एक कमजोरी है जिसका खतरा स्रोत द्वारा शोषण किया जा सकता है।", "options": ["Threat", "Vulnerability", "Control", "Attack"], "answer": "Vulnerability"})

quiz_data.append({"section": sect, "q_eng": "Which of the following file formats is used for Java Server Page?", "q_hin": "जावा सर्वर पेज के लिए किस फाइल फॉर्मेट का उपयोग किया जाता है?", "options": [".js", ".java", ".jsp", ".jspl"], "answer": ".jsp"})

quiz_data.append({"section": sect, "q_eng": "File format WPD is used for which of the following files?", "q_hin": "फाइल फॉर्मेट WPD का उपयोग किस फाइल के लिए किया जाता है?", "options": ["Image File", "Compressed Archive File", "Winamp Playlist", "WordPerfect Document File"], "answer": "WordPerfect Document File"})

quiz_data.append({"section": sect, "q_eng": "What is the full form of UPS?", "q_hin": "UPS का पूर्ण रूप क्या है?", "options": ["Uninterruptible power supply", "Unified power supply", "Uninterruptible power sink", "Universal power sink"], "answer": "Uninterruptible power supply"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is included along with genuine software, and may come from a malicious website?", "q_hin": "इनमें से किसे वास्तविक सॉफ़्टवेयर के साथ शामिल किया जाता है और यह किसी मैलिसियस वेबसाइट से आया हो सकता है?", "options": ["Spyware", "VMware", "Middleware", "Adware"], "answer": "Spyware"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is NOT a benefit of Software Testing?", "q_hin": "निम्नलिखित में से कौन-सा सॉफ्टवेयर परीक्षण का लाभ नहीं है?", "options": ["Bug free application", "Cost effective", "Low failure", "Gathering requirements"], "answer": "Gathering requirements"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is NOT a valid email prefix format?", "q_hin": "निम्नलिखित में से कौन सा वैध ईमेल उपसर्ग प्रारूप नहीं है?", "options": ["xyz-d@mail.com", "xyz.mnp@mail.com", "xyz-@mail.com", "xyz@mail.com"], "answer": "xyz-@mail.com"})

quiz_data.append({"section": sect, "q_eng": "With reference to computer networks, what is the full form of OSI?", "q_hin": "कंप्यूटर नेटवर्क के संदर्भ में OSI का पूर्ण रूप क्या है?", "options": ["Open Systems Interconnection", "Open Source Interconnection", "Open Systems Internet", "Open Static Interconnection"], "answer": "Open Systems Interconnection"})

quiz_data.append({"section": sect, "q_eng": "____________ is unsolicited internet content that is typically sent in bulk for advertising purposes.", "q_hin": "____________ ऐसी अवांछित इंटरनेट सामग्री है जो विज्ञापन उद्देश्यों के लिए थोक में भेजी जाती है।", "options": ["Spam", "Cookies", "Firewall", "Phishing"], "answer": "Spam"})

quiz_data.append({"section": sect, "q_eng": "When inserting page number in footer of MS-Word 2019, number 2 appears but you want 'b' letter. How to change?", "q_hin": "MS-Word 2019 डॉक्युमेंट के फुटर में पेज नंबर डालते समय 2 दिखता है, आप अक्षर b दिखाना चाहते हैं। क्या करेंगे?", "options": ["From Insert tab specify settings", "Go to Layout click format", "From Format choose bullets", "Go to Mailings specify settings"], "answer": "From Insert tab specify settings"})

quiz_data.append({"section": sect, "q_eng": "In MS-Word 2019, the space between tabs can show dots, dashes etc. These are called ____________.", "q_hin": "MS-Word 2019 में टैब्स के बीच का स्थान डॉट्स, डैश आदि दिखा सकता है। इन्हें ____________ कहा जाता है।", "options": ["Decimal characters", "Space characters", "Leader characters", "Extra characters"], "answer": "Leader characters"})

quiz_data.append({"section": sect, "q_eng": "In a network, ____________ measures the time it takes for some data to get to its destination. It is a measure of delay.", "q_hin": "नेटवर्क में ____________ डेटा को अपने गंतव्य तक पहुंचने में लगने वाले समय को मापता है। यह विलंब का माप होता है।", "options": ["Network latency", "Bandwidth", "Frequency", "Wavelength"], "answer": "Network latency"})

quiz_data.append({"section": sect, "q_eng": "Which is NOT a valid option for setting up type of letters in second step of Mail Merge in MS-Word 2019?", "q_hin": "MS-Word 2019 में मेल मर्ज प्रक्रिया के दूसरे चरण में लेटर्स के प्रकार को सेट करने के लिए कौन-सा विकल्प वैध नहीं है?", "options": ["Use the current document", "Start from a template", "Start from existing document", "Start using current document"], "answer": "Start using current document"})

quiz_data.append({"section": sect, "q_eng": "How many radio buttons are under Select Starting Document for letters in Mail Merge step 2?", "q_hin": "MS-Word 2019 में मेल मर्ज प्रक्रिया के दूसरे चरण में 'Select Starting Document' के अंतर्गत कितने रेडियो बटन होते हैं?", "options": ["one", "two", "three", "four"], "answer": "three"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is NOT a search engine?", "q_hin": "इनमें से कौन-सा एक सर्च इंजन नहीं है?", "options": ["Microsoft Bing", "Google.com", "Coursera", "Yahoo.com"], "answer": "Coursera"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is an address that identifies a process on a host?", "q_hin": "निम्नलिखित में से कौन सा एड्रेस है जो किसी होस्ट पर एक प्रोसेस की पहचान करता है?", "options": ["IP address", "Port number", "Network address", "MAC address"], "answer": "Port number"})

quiz_data.append({"section": sect, "q_eng": "In MS-Word 2019, if Save button is NOT available in Quick Access toolbar, what must be done to add it?", "q_hin": "MS-Word 2019 में यदि क्विक एक्सेस टूलबार में सेव बटन उपलब्ध नहीं है, तो उसे जोड़ने के लिए क्या करना चाहिए?", "options": ["Go to File -> Drag open", "Double-click on toolbar", "Click down arrow on right side -> Click Save", "Go to File -> Save"], "answer": "Click down arrow on right side -> Click Save"})

quiz_data.append({"section": sect, "q_eng": "A ____________ is a device that converts digital computer signals into an analog signal form to travel over phone lines.", "q_hin": "____________ एक उपकरण है जो डिजिटल कंप्यूटर सिग्नल को एनालॉग सिग्नल में परिवर्तित करता है जो फोन लाइनों पर यात्रा कर सकता है।", "options": ["Router", "Hub", "Modem", "Codec"], "answer": "Modem"})

quiz_data.append({"section": sect, "q_eng": "Which Ethernet Cable is made of glass cores surrounded by several layers of covering material?", "q_hin": "कौन सी ईथरनेट केबल ग्लास कोर से बनी होती है जो कई परतों से घिरी होती है?", "options": ["Twisted pair cable", "Coaxial cable", "Fibre optic cable", "Unshielded twisted pair"], "answer": "Fibre optic cable"})

quiz_data.append({"section": sect, "q_eng": "To create a graph in MS-Excel 2019, which of the following steps must be taken?", "q_hin": "MS-Excel 2019 में ग्राफ बनाने के लिए किन चरणों का उपयोग किया जाता है?", "options": ["File tab -> Charts", "Home tab -> Charts", "Insert tab -> Recommended Charts", "View tab -> Charts"], "answer": "Insert tab -> Recommended Charts"})

quiz_data.append({"section": sect, "q_eng": "A chart ____________ is a brief, descriptive label that summarizes the main point or purpose of the graph.", "q_hin": "चार्ट ____________ एक संक्षिप्त लेबल है जो ग्राफ के मुख्य बिंदु या उद्देश्य को सारांशित करता है।", "options": ["axes", "title", "source", "legend"], "answer": "title"})

quiz_data.append({"section": sect, "q_eng": "Which of the following keyboard shortcuts is used to make letters italic in MS-Excel 2019?", "q_hin": "MS-Excel 2019 में अक्षरों को इटैलिक करने के लिए किस कीबोर्ड शॉर्टकट का उपयोग किया जाता है?", "options": ["Ctrl + I", "Ctrl + B", "Ctrl + U", "Ctrl + V"], "answer": "Ctrl + I"})

quiz_data.append({"section": sect, "q_eng": "Which of the following keyboard shortcuts is used to hide a row in MS-Excel 2019?", "q_hin": "MS-Excel 2019 में एक पंक्ति को छिपाने के लिए किस कीबोर्ड शॉर्टकट का उपयोग किया जाता है?", "options": ["Ctrl + 9", "Ctrl + 0", "Ctrl + 1", "Ctrl + 2"], "answer": "Ctrl + 9"})

quiz_data.append({"section": sect, "q_eng": "A sports teacher recorded scores in Excel 2019. He wants to find total scores. Which function should he use?", "q_hin": "एक खेल शिक्षक ने MS-Excel 2019 में अंक दर्ज किए। अब वह कुल अंक ज्ञात करना चाहता है। उसे किस फंक्शन का उपयोग करना चाहिए?", "options": ["COUNT", "ADD", "SUM", "TOTAL"], "answer": "SUM"})

quiz_data.append({"section": sect, "q_eng": "A teacher wants to arrange student marks in ascending order. Which option within Data tab should she use?", "q_hin": "एक शिक्षिका MS-Excel 2019 में डेटा को आरोही क्रम में व्यवस्थित करना चाहती है। उसे किस विकल्प का उपयोग करना चाहिए?", "options": ["Sort", "Format", "Filter", "Data Tools"], "answer": "Sort"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is NOT a benefit of using MS-Excel charts?", "q_hin": "MS-Excel चार्ट्स का उपयोग करने का कौन सा लाभ नहीं है?", "options": ["Visual representation of data", "Easy comparison", "Automatic error correction", "Trend analysis"], "answer": "Automatic error correction"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to check spelling in MS-Word 2019?", "q_hin": "MS-Word 2019 में स्पेलिंग जांचने के लिए किसका उपयोग किया जाता है?", "options": ["Spell Check", "AutoCorrect", "Grammar Tool", "Dictionary"], "answer": "Spell Check"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is a shortcut to insert a new slide in MS-PowerPoint 2019?", "q_hin": "MS-PowerPoint 2019 में नई स्लाइड डालने का शॉर्टकट कौन सा है?", "options": ["Ctrl + M", "Ctrl + N", "Ctrl + S", "Ctrl + L"], "answer": "Ctrl + M"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to create a table in MS-Word 2019?", "q_hin": "MS-Word 2019 में टेबल बनाने के लिए किसका उपयोग किया जाता है?", "options": ["Insert -> Table", "Layout -> Table", "View -> Table", "Format -> Table"], "answer": "Insert -> Table"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is NOT a valid data type in MS-Excel 2019?", "q_hin": "MS-Excel 2019 में कौन सा वैध डेटा प्रकार नहीं है?", "options": ["Number", "Text", "Date", "Paragraph"], "answer": "Paragraph"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to insert a chart in MS-Excel 2019?", "q_hin": "MS-Excel 2019 में चार्ट डालने के लिए किसका उपयोग किया जाता है?", "options": ["Insert -> Chart", "Data -> Chart", "Format -> Chart", "View -> Chart"], "answer": "Insert -> Chart"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to apply bold formatting in MS-Word 2019?", "q_hin": "MS-Word 2019 में बोल्ड फॉर्मेटिंग लगाने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + B", "Ctrl + I", "Ctrl + U", "Ctrl + V"], "answer": "Ctrl + B"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to save a file in MS-Word 2019?", "q_hin": "MS-Word 2019 में फाइल सेव करने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + S", "Ctrl + P", "Ctrl + O", "Ctrl + N"], "answer": "Ctrl + S"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to print a document in MS-Word 2019?", "q_hin": "MS-Word 2019 में डॉक्युमेंट प्रिंट करने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + P", "Ctrl + S", "Ctrl + O", "Ctrl + N"], "answer": "Ctrl + P"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to open a new document in MS-Word 2019?", "q_hin": "MS-Word 2019 में नया डॉक्युमेंट खोलने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + N", "Ctrl + O", "Ctrl + S", "Ctrl + P"], "answer": "Ctrl + N"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to close a document in MS-Word 2019?", "q_hin": "MS-Word 2019 में डॉक्युमेंट बंद करने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + W", "Ctrl + Q", "Ctrl + E", "Ctrl + R"], "answer": "Ctrl + W"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to insert a hyperlink in MS-Word 2019?", "q_hin": "MS-Word 2019 में हाइपरलिंक डालने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + K", "Ctrl + H", "Ctrl + L", "Ctrl + J"], "answer": "Ctrl + K"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to undo the last action in MS-Word 2019?", "q_hin": "MS-Word 2019 में अंतिम क्रिया को पूर्ववत करने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + C"], "answer": "Ctrl + Z"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to redo the last action in MS-Word 2019?", "q_hin": "MS-Word 2019 में अंतिम क्रिया को फिर से करने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + Y", "Ctrl + Z", "Ctrl + X", "Ctrl + C"], "answer": "Ctrl + Y"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to cut selected text in MS-Word 2019?", "q_hin": "MS-Word 2019 में चयनित टेक्स्ट को काटने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + X", "Ctrl + C", "Ctrl + V", "Ctrl + Z"], "answer": "Ctrl + X"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to copy selected text in MS-Word 2019?", "q_hin": "MS-Word 2019 में चयनित टेक्स्ट को कॉपी करने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + C", "Ctrl + X", "Ctrl + V", "Ctrl + Z"], "answer": "Ctrl + C"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to paste copied text in MS-Word 2019?", "q_hin": "MS-Word 2019 में कॉपी किए गए टेक्स्ट को पेस्ट करने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + V", "Ctrl + C", "Ctrl + X", "Ctrl + Z"], "answer": "Ctrl + V"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to select all text in MS-Word 2019?", "q_hin": "MS-Word 2019 में सभी टेक्स्ट को चुनने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + A", "Ctrl + S", "Ctrl + D", "Ctrl + F"], "answer": "Ctrl + A"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to find text in MS-Word 2019?", "q_hin": "MS-Word 2019 में टेक्स्ट खोजने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + F", "Ctrl + A", "Ctrl + S", "Ctrl + D"], "answer": "Ctrl + F"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to replace text in MS-Word 2019?", "q_hin": "MS-Word 2019 में टेक्स्ट बदलने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + H", "Ctrl + F", "Ctrl + R", "Ctrl + E"], "answer": "Ctrl + H"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to open the Font dialog box in MS-Word 2019?", "q_hin": "MS-Word 2019 में फॉन्ट डायलॉग बॉक्स खोलने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + D", "Ctrl + F", "Ctrl + G", "Ctrl + H"], "answer": "Ctrl + D"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to open the Paragraph dialog box in MS-Word 2019?", "q_hin": "MS-Word 2019 में पैराग्राफ डायलॉग बॉक्स खोलने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + E", "Ctrl + P", "Ctrl + M", "Alt + O"], "answer": "Ctrl + M"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to insert a new worksheet in MS-Excel 2019?", "q_hin": "MS-Excel 2019 में नई वर्कशीट डालने के लिए किसका उपयोग किया जाता है?", "options": ["Shift + F11", "Ctrl + N", "Ctrl + W", "Alt + S"], "answer": "Shift + F11"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to insert a new slide in MS-PowerPoint 2019?", "q_hin": "MS-PowerPoint 2019 में नई स्लाइड डालने के लिए किसका उपयोग किया जाता है?", "options": ["Ctrl + M", "Ctrl + N", "Ctrl + S", "Ctrl + L"], "answer": "Ctrl + M"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to refresh a webpage in most browsers?", "q_hin": "अधिकांश ब्राउज़रों में वेबपेज को रिफ्रेश करने के लिए किसका उपयोग किया जाता है?", "options": ["F5", "F2", "Ctrl + R", "Ctrl + F"], "answer": "F5"})

quiz_data.append({"section": sect, "q_eng": "Which of the following is used to permanently delete a file in Windows without sending it to Recycle Bin?", "q_hin": "Windows में किसी फाइल को रीसायकल बिन में भेजे बिना स्थायी रूप से हटाने के लिए किसका उपयोग किया जाता है?", "options": ["Shift + Delete", "Ctrl + Delete", "Alt + Delete", "Esc"], "answer": "Shift + Delete"})
# --- QUIZ UI LOGIC ---

st.markdown("<h1 class='header-text'>🎓 CPCT QUIZ</h1>", unsafe_allow_html=True)
st.markdown("<div class='gold-line'></div>", unsafe_allow_html=True)

score = 0

for idx, q in enumerate(quiz_data, start=1):
    st.markdown(f"<div class='section-badge'>{q['section']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='question-box'>{idx}. {q['q_eng']}<br><span class='hindi-text'>{q['q_hin']}</span></div>", unsafe_allow_html=True)
    
    user_ans = st.radio(f"Select your answer for Q{idx}:", q["options"], key=f"q{idx}")
    
    if user_ans == q["answer"]:
        score += 1

# --- RESULT ---
if st.button("Submit Quiz"):
    st.success(f"✅ You scored {score} out of {len(quiz_data)}")
    st.markdown("<div class='gold-line'></div>", unsafe_allow_html=True)
    if score == len(quiz_data):
        st.balloons()
        st.info("🎉 Perfect Score! Excellent work Aneesh!")
    elif score >= len(quiz_data) * 0.7:
        st.info("👏 Great job! You passed with a good score.")
    else:
        st.warning("Keep practicing! You can improve with more revision.")

# --- LOGIN SCREEN ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<div class='main-card'><h2 class='header-text'>🔐 Login</h2></div>", unsafe_allow_html=True)
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if username == "aneesh" and password == "1234":   # तुम चाहो तो यहाँ अपना पासवर्ड बदल सकते हो
            st.session_state.logged_in = True
            st.success("✅ Login Successful!")
        else:
            st.error("❌ Invalid Username or Password")
    st.stop()

# --- QUIZ SCREEN ---
st.markdown("<h1 class='header-text'>🎓 CPCT QUIZ</h1>", unsafe_allow_html=True)
st.markdown("<div class='gold-line'></div>", unsafe_allow_html=True)

score = 0

for idx, q in enumerate(quiz_data, start=1):
    st.markdown(f"<div class='section-badge'>{q['section']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='question-box'>{idx}. {q['q_eng']}<br><span class='hindi-text'>{q['q_hin']}</span></div>", unsafe_allow_html=True)
    
    user_ans = st.radio(f"Select your answer for Q{idx}:", q["options"], key=f"q{idx}")
    
    if user_ans == q["answer"]:
        score += 1

# --- RESULT SCREEN ---
if st.button("Submit Quiz"):
    st.success(f"✅ You scored {score} out of {len(quiz_data)}")
    st.markdown("<div class='gold-line'></div>", unsafe_allow_html=True)
    if score == len(quiz_data):
        st.balloons()
        st.info("🎉 Perfect Score! Excellent work Aneesh!")
    elif score >= len(quiz_data) * 0.7:
        st.info("👏 Great job! You passed with a good score.")
    else:
        st.warning("Keep practicing! You can improve with more revision.")
