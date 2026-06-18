import streamlit as st

# Page configuration for mobile view
st.set_page_config(page_title="ANEESH MAKE CPCT QUIZ", page_icon="🎓", layout="centered")

# --- 1. NEON GOLD GLOW CSS FOR PREMIUM LOOK ---
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

for i in range(1, 76):
    # --- COMPUTER PROFICIENCY SECTION (Q1 to Q52) ---
    if i <= 52:
        sect = "Computer Proficiency & IT Skills"
        if i == 1:
            q_eng = "Cache and main memory will lose their contents when the power of a computer is off. This property is referred to as ____________."
            q_hin = "कैश और मुख्य मेमोरी अपनी सामग्री (कंटेन्ट) खो देंगे जब बिजली बंद हो जाएगी, इस गुण को ____________ के रूप में संदर्भित किया जाता हैं।"
            opts = ["Dynamic (डायनमिक)", "Static (स्टैटिक)", "Volatility (वोलैटिलिटी)", "Non-volatile (नॉन-वोलेटाइल)"]
            ans = "Volatility (वोलैटिलिटी)"
        elif i == 2:
            q_eng = "Which of the following is a set of instructions embedded on a piece of hardware at the time of manufacturing and tells the device how to operate?"
            q_hin = "निम्नलिखित में से कौन सा हार्डवेयर के निर्माण के समय उस पर सन्निहित निर्देशों का एक सेट है और डिवाइस को संचालित करने का तरीका बताता है?"
            opts = ["Application Software (एप्लिकेशन सॉफ्टवेयर)", "Utility Software (यूटिलिटी सॉफ्टवेयर)", "Firmware (फर्मवेयर)", "Freeware (फ्रीवेयर)"]
            ans = "Firmware (फर्मवेयर)"
        elif i == 3:
            q_eng = "____________ is a programmable device that takes in input, performs some arithmetic and logical operations over it and produces the desired output."
            q_hin = "____________ एक प्रोग्राम करने योग्य डिवाइस है जो इनपुट लेता है, उस पर कुछ अंकगणितीय और तार्किक ऑपरेशन करता है और वांछित आउटपुट उत्पन्न करता है।"
            opts = ["SMPS (एसएमपीएस)", "UPS (यूपीएस)", "Microprocessor (माइक्रोप्रोसेसर)", "Bus (बस)"]
            ans = "Microprocessor (माइक्रोप्रोसेसर)"
        elif i == 4:
            q_eng = "You CANNOT save an MS-Excel 2016 file in a/an ____________ format."
            q_hin = "आप MS-Excel 2016 फाइल को ____________ फ़ॉर्मेट में सेव नहीं कर सकते।"
            opts = ["PDF", "PSD", "TXT", "XML"]
            ans = "PSD"
        elif i == 5:
            q_eng = "What does the term SCSI stand for?"
            q_hin = "SCSI का पूर्ण रूप ____________ है।"
            opts = ["Small Computer Software Interface", "Small Computer Storage Interface", "Small Computer System Interface", "Small Computer Standard Interface"]
            ans = "Small Computer System Interface"
        elif i == 6:
            q_eng = "The most common input devices are:"
            q_hin = "इनमे से सबसे आम इनपुट डिवाइस कौन-size हैं?"
            opts = ["Microphone and Printer (माइक्रोफोन और प्रिंटर)", "Scanner and Monitor (स्कैनर और मॉनीटर)", "Digital Camera and Speaker (डिजिटल कैमरा और स्पीकर)", "Keyboard and Mouse (कीबोर्ड और माउस)"]
            ans = "Keyboard and Mouse (कीबोर्ड और माउस)"
        elif i == 7:
            q_eng = "In a computer, which device is functionally opposite to a keyboard?"
            q_hin = "एक कंप्यूटर में, कौन-sa डिवाइस कार्यात्मक रूप से कीबोर्ड से विपरीत है?"
            opts = ["Joystick (जॉयस्टिक)", "Track ball (ट्रेक बॉल)", "Mouse (माउस)", "Printer (प्रिंटर)"]
            ans = "Printer (प्रिंटर)"
        elif i == 8:
            q_eng = "Which of the following is Python language editor?"
            q_hin = "इनमें से कौन पायथन भाषा संपादक है?"
            opts = ["Tally (टैली)", "Coda (कोडा)", "Jupyter (जुपिटर)", "SnapTouch (स्नैपटच)"]
            ans = "Jupyter (जुपिटर)"
        elif i == 9:
            q_eng = "Which of the following is utility software?"
            q_hin = "निम्नलिखित में से कौनसा यूटिलिटी सॉफ्टवेयर है?"
            opts = ["Avast Antivirus (एवास्ट एंटीवायरस)", "BIOS", "Android (एंड्रॉइड)", "MS-Word"]
            ans = "Avast Antivirus (एवास्ट एंटीवायरस)"
        elif i == 10:
            q_eng = "Which of the following is true with reference to DVD?"
            q_hin = "DVD के संदर्भ में निम्नलिखित में से कौन सा सत्य है?"
            opts = ["Full form of DVD is Digital Valid Disk.", "DVDs are not portable.", "DVD-R offers a write once approach.", "DVD ROM is used for both reading and writing."]
            ans = "DVD-R offers a write once approach."
        elif i == 11:
            q_eng = "Which of the following is an example of open source software?"
            q_hin = "निम्नलिखित में से कौन सा ओपन सोर्स सॉफ्टवेयर का एक उदाहरण है?"
            opts = ["Netflix (नेटफ्लिक्स)", "MySQL", "McAfee (मैकएफी)", "Google Chrome (गूगल क्रोम)"]
            ans = "MySQL"
        elif i == 12:
            q_eng = "Which of the following plotters draws exact vector graphics on paper or other media?"
            q_hin = "निम्नलिखित में से कौन सा प्लॉटर कागज़ या अन्य मीडिया पर सटीक वेक्टर ग्राफ़िक्स बनाता है?"
            opts = ["Cutting Plotter (कटिंग प्लॉटर)", "Pinch Roller (पिंच रोलर)", "Cycle Plotter (साइकिल प्लॉटर)", "Drum Plotter (ड्रम प्लॉटर)"]
            ans = "Drum Plotter (ड्रम प्लॉटर)"
        elif i == 13:
            q_eng = "____________ is an internet service consisting of thousands of newsgroups."
            q_hin = "____________ एक इंटरनेट सेवा है जिसमें हजारों समाचार समूह शामिल हैं।"
            opts = ["USECASE", "USENET", "USESET", "UCENET"]
            ans = "USENET"
        elif i == 14:
            q_eng = "Which of the following keyboard shortcut keys is used to rename a highlighted icon, file or folder in Windows 10?"
            q_hin = "Windows 10 में हाइलाइट किए गए आइकन, फाइल या फोल्डर का नाम बदलने के लिए निम्न में से किस कीबोर्ड शॉर्टकट कुंजी का उपयोग किया जाता है?"
            opts = ["F3", "F5", "F2", "F4"]
            ans = "F2"
        elif i == 15:
            q_eng = "Cortana is an intelligent personal assistant developed by ____________."
            q_hin = "कॉर्टाना (Cortana) ____________ द्वारा विकसित एक बुद्धिमान व्यक्तिगत सहायक है।"
            opts = ["Microsoft (माइक्रोसोफ्ट)", "Apple (एप्पल)", "HP (एचपी)", "Oracle (ओरेकल)"]
            ans = "Microsoft (माइक्रोसोफ्ट)"
        elif i == 16:
            q_eng = "Which of the following devices is commonly used to protect an internal network from unwanted access?"
            q_hin = "अवांछित पहुंच (एक्सेस) से आंतरिक नेटवर्क की सुरक्षा के लिए आमतौर पर कौन-सा डिवाइस उपयोग किया जाता है?"
            opts = ["Firewall (फ़ायरवॉल)", "Router (राउटर)", "Switch (स्विच)", "Hub (हब)"]
            ans = "Firewall (फ़ायरवॉल)"
        elif i == 17:
            q_eng = "Which of the following statements is/are true? (i) GUI actions are through direct manipulation. (ii) Dialogue box asks for input."
            q_hin = "निम्नलिखित में से कौन-sa कथन सत्य है/हैं? (i) GUI में क्रियाएं आमतौर पर बटन और आइकन के सीधे हेरफेर से होती हैं। (ii) डायलॉग बॉक्स उपयोगकर्ता से इनपुट मांगता है।"
            opts = ["Only (i)", "Only (ii)", "Both (i) and (ii) ((i) और (ii) दोनों)", "Neither (i) nor (ii)"]
            ans = "Both (i) and (ii) ((i) और (ii) दोनों)"
        elif i == 18:
            q_eng = "A grey scale picture in JPEG is divided into blocks of ____________ pixels."
            q_hin = "JPEG में एक ग्रे स्केल चित्र, ____________ पिक्सल के ब्लॉक में विभाजित होती है।"
            opts = ["6x6", "5x5", "7x7", "8x8"]
            ans = "8x8"
        elif i == 19:
            q_eng = "Which of the following ranges across countries and continents? (i) LAN (ii) MAN (iii) WAN"
            q_hin = "निम्नलिखित में से किसकी रेंज देश और महाद्वीपों तक होती है? (i) LAN (ii) MAN (iii) WAN"
            opts = ["Only (i) / केवल (i)", "Only (ii) / केवल (ii)", "Only (iii) / केवल (iii)", "Both (i) and (ii)"]
            ans = "Only (iii) / केवल (iii)"
        elif i == 20:
            q_eng = "The security property which defines the ability of a system to ensure that an asset is modified only by authorised parties is called ____________."
            q_hin = "सुरक्षा संपत्ति जो यह सुनिश्चित करती है कि एक संपत्ति केवल अधिकृत पार्टियों द्वारा संशोधित की जाती है, उसे ____________ कहा जाता है।"
            opts = ["Availability (उपलब्धता)", "Confidentiality (गोपनीयता)", "Integrity (अखंडता)", "Cryptograph"]
            ans = "Integrity (अखंडता)"
        elif i == 21:
            q_eng = "How to view the MAC address associated with Windows 10 Ethernet device?"
            q_hin = "Windows 10 ईथरनेट डिवाइस से जुड़े MAC पते को कैसे देखें?"
            opts = ["Settings->Network and Internet->Status->Properties", "Settings->Dial-up->Properties", "Settings->VPN->Properties", "Settings->Proxy->Properties"]
            ans = "Settings->Network and Internet->Status->Properties"
        elif i == 22:
            q_eng = "AES symmetric encryption algorithm performs all its computations on ____________ of data rather than in bits."
            q_hin = "एईएस (AES) सममित एन्क्रिप्शन एल्गोरिथ्म बिट्स के बजाय डेटा के ____________ पर अपनी सभी गणना करता है।"
            opts = ["Bytes (बाइट्स)", "Numbers", "Cells", "Digits"]
            ans = "Bytes (बाइट्स)"
        elif i == 23:
            q_eng = "When a router needs to send a packet to another computer/network, then it should know which of the following?"
            q_hin = "जब किसी राउटर को एक पैकेट को दूसरे कंप्यूटर नेटवर्क में भेजने की आवश्यकता होती है, तो उसे क्या पता होना चाहिए?"
            opts = ["Datagram", "Path name", "Transport medium", "IP address (IP एड्रेस)"]
            ans = "IP address (IP एड्रेस)"
        elif i == 24:
            q_eng = "How is the computer monitor size measured?"
            q_hin = "मॉनिटर का आकार (माप) कैसे मापा जाता है?"
            opts = ["From left top to left bottom", "From right top to right bottom", "From corner to corner diagonally (कोने से कोने तक)", "From left top to right top"]
            ans = "From corner to corner diagonally (कोने से कोने तक)"
        elif i == 25:
            q_eng = "A/an ____________ is a weakness in an information system, system security procedures, or internal controls that could be exploited by a threat source."
            q_hin = "____________ एक सूचना प्रणाली, सिस्टम सुरक्षा प्रक्रियाओं या आंतरिक नियंत्रण में एक कमजोरी है जिसका खतरा स्रोत द्वारा शोषण किया जा सकता है।"
            opts = ["Threat", "Vulnerability (वल्नेरेबिलिटी)", "Control", "Attack"]
            ans = "Vulnerability (वल्नेरेबिलिटी)"
        elif i == 26:
            q_eng = "Which of the following file formats is used for Java Server Page?"
            q_hin = "जावा सर्वर पेज (Java Server Page) के लिए निम्नलिखित में से किस फाइल फॉर्मेट का उपयोग किया जाता है?"
            opts = [".js", ".java", ".jsp", ".jspl"]
            ans = ".jsp"
        elif i == 27:
            q_eng = "File format WPD is used for which of the following files?"
            q_hin = "फाइल फॉर्मेट WPD का उपयोग निम्नलिखित में से किस फाइल के लिए किया जाता है?"
            opts = ["Image File", "Compressed Archive File", "Winamp Playlist", "WordPerfect Document File"]
            ans = "WordPerfect Document File"
        elif i == 28:
            q_eng = "What is the full form of UPS?"
            q_hin = "यूपीएस (UPS) का पूर्ण रूप क्या है?"
            opts = ["Uninterruptible power supply", "Unified power supply", "Uninterruptible power sink", "Universal power sink"]
            ans = "Uninterruptible power supply"
        elif i == 29:
            q_eng = "Which of the following is included along with genuine software, and may come from a malicious website?"
            q_hin = "इनमें से किसे वास्तविक सॉफ़्टवेयर के साथ शामिल किया जाता है और यह किसी मैलिसियस वेबसाइट से आया हो सकता है?"
            opts = ["Spyware (स्पाईवेयर)", "VMware", "Middleware", "Adware"]
            ans = "Spyware (स्पाईवेयर)"
        elif i == 30:
            q_eng = "Which of the following is NOT a benefit of Software Testing?"
            q_hin = "निम्नलिखित में से कौन-sa, सॉफ्टवेयर परीक्षण का लाभ नहीं है?"
            opts = ["Bug free application", "Cost effective", "Low failure", "Gathering requirements (आवश्यकताओं को इकट्ठा करना)"]
            ans = "Gathering requirements (आवश्यकताओं को इकट्ठा करना)"
        elif i == 31:
            q_eng = "Which of the following is NOT a valid email prefix format?"
            q_hin = "निम्नलिखित में से कौन सा वैध ईमेल उपसर्ग प्रारूप नहीं है?"
            opts = ["xyz-d@mail.com", "xyz.mnp@mail.com", "xyz-@mail.com", "xyz@mail.com"]
            ans = "xyz-@mail.com"
        elif i == 32:
            q_eng = "With reference to computer networks, what is the full form of OSI?"
            q_hin = "कंप्यूटर नेटवर्क के संदर्भ में, OSI का पूर्ण रूप क्या है?"
            opts = ["Open Systems Interconnection", "Open Source Interconnection", "Open Systems Internet", "Open Static Interconnection"]
            ans = "Open Systems Interconnection"
        elif i == 33:
            q_eng = "____________ is unsolicited internet content that is typically sent in bulk for advertising purposes."
            q_hin = "____________ ऐसी अवांछित इंटरनेट सामग्री है जो विज्ञापन उद्देश्यों के लिए थोक में भेजी जाती है।"
            opts = ["Spam (स्पैम)", "Cookies", "Firewall", "Phishing"]
            ans = "Spam (स्पैम)"
        elif i == 34:
            q_eng = "When inserting page number in footer of MS-Word 2019, number 2 appears but you want 'b' letter. How to change?"
            q_hin = "जब आप MS-Word 2019 डॉक्युमेंट के फुटर में पेज नंबर डालते हैं तो 2 दिखता है, आप अक्षर b दिखाना चाहते हैं। क्या करेंगे?"
            opts = ["From Insert tab specify settings", "Go to Layout click format", "From Format choose bullets", "Go to Mailings specify settings"]
            ans = "From Insert tab specify settings"
        elif i == 35:
            q_eng = "In MS-Word 2019, the space between tabs can show dots, dashes etc. These are called ____________."
            q_hin = "MS-Word 2019 में, टैब के बीच का स्थान डॉट्स, डैश आदि दिखा सकता है। इन्हें ____________ कहा जाता है।"
            opts = ["Decimal characters", "Space characters", "Leader characters (लीडर कैरेक्टर्स)", "Extra characters"]
            ans = "Leader characters (लीडर कैरेक्टर्स)"
        elif i == 36:
            q_eng = "In a network, ____________ measures the time it takes for some data to get to its destination. It is a measure of delay."
            q_hin = "नेटवर्क में, ____________ डेटा को अपने गंतव्य तक पहुंचने में लगने वाले समय को मापता है। यह विलंब का माप होता है।"
            opts = ["Network latency (नेटवर्क लेटेंसी)", "Bandwidth", "Frequency", "Wavelength"]
            ans = "Network latency (नेटवर्क लेटेंसी)"
        elif i == 37:
            q_eng = "Which is NOT a valid option for setting up type of letters in second step of Mail Merge in MS-Word 2019?"
            q_hin = "MS-Word 2019 में मेल मर्ज प्रक्रिया के दूसरे चरण में लेटर्स के प्रकार को सेट करने के लिए कौन-sa एक वैध विकल्प नहीं है?"
            opts = ["Use the current document", "Start from a template", "Start from existing document", "Start using current document"]
            ans = "Start using current document"
        elif i == 38:
            q_eng = "How many radio buttons are under Select Starting Document for letters in Mail Merge step 2?"
            q_hin = "MS-Word 2019 में मेल मर्ज प्रक्रिया के दूसरे चरण में पत्रों के लिए 'Select Starting Document' के अंतर्गत कितने रेडियो बटन होते हैं?"
            opts = ["one (एक)", "two (दो)", "three (तीन)", "four (चार)"]
            ans = "three (तीन)"
        elif i == 39:
            q_eng = "Which of the following is NOT a search engine?"
            q_hin = "इनमें से कौन-sa, एक सर्च engine नहीं है?"
            opts = ["Microsoft Bing", "Google.com", "Coursera", "Yahoo.com"]
            ans = "Coursera"
        elif i == 40:
            q_eng = "Which of the following is an address that identifies a process on a host?"
            q_hin = "निम्नलिखित में से कौन-sa, एक एड्रेस है जो किसी होस्ट पर एक प्रोसेस की पहचान करता है?"
            opts = ["IP address", "Port number (पोर्ट नंबर)", "Network address", "MAC address"]
            ans = "Port number (पोर्ट नंबर)"
        elif i == 41:
            q_eng = "In MS-Word 2019, if Save button is NOT available in Quick Access toolbar, what must be done to add it?"
            q_hin = "MS-Word 2019 में यदि क्विक एक्सेस टूलबार में सेव बटन उपलब्ध नहीं है, तो उसे जोड़ने के लिए क्या किया जाना चाहिए?"
            opts = ["Go to File -> Drag open", "Double-click on toolbar", "Click down arrow on right side -> Click Save", "Go to File -> Save"]
            ans = "Click down arrow on right side -> Click Save"
        elif i == 42:
            q_eng = "A ____________ is a device that converts digital computer signals into an analog signal form to travel over phone lines."
            q_hin = "____________ एक उपकरण है जो डिजिटल computer सिग्नल को एक एनालॉग सिग्नल रूप में परिवर्तित करता है जो फोन लाइनों पर यात्रा कर सकता है।"
            opts = ["Router", "Hub", "Modem (मॉडेम)", "Codec"]
            ans = "Modem (मॉडेम)"
        elif i == 43:
            q_eng = "Which Ethernet Cable is made of glass cores surrounded by several layers of covering material?"
            q_hin = "कौन सी ईथरनेट केबल ग्लास कोर से बनी होती है जो आमतौर पर आवरण सामग्री की कई परतों से घिरी होती है?"
            opts = ["Twisted pair cable", "Coaxial cable", "Fibre optic cable (फाइबर ऑप्टिक केबल)", "Unshielded twisted pair"]
            ans = "Fibre optic cable (फाइबर ऑप्टिक केबल)"
        elif i == 44:
            q_eng = "To create a graph in MS-Excel 2019, which of the following steps must be taken?"
            q_hin = "MS-Excel 2019 में ग्राफ बनाने के लिए निम्नलिखित में से किन चरणों का उपयोग किया जाता है?"
            opts = ["File tab -> Charts", "Home tab -> Charts", "Insert tab -> Recommended Charts", "View tab -> Charts"]
            ans = "Insert tab -> Recommended Charts"
        elif i == 45:
            q_eng = "A chart ____________ is a brief, descriptive label that summarizes the main point or purpose of the graph."
            q_hin = "चार्ट ____________ एक संक्षिप्त, वर्णनात्मक लेबल है जो ग्राफ के मुख्य बिंदु या उद्देश्य को सारांशित करता है।"
            opts = ["axes", "title (टाइटल)", "source", "legend"]
            ans = "title (टाइटल)"
        elif i == 46:
            q_eng = "Which of the following keyboard shortcuts is used to make letters italic in MS-Excel 2019?"
            q_hin = "MS-Excel 2019 में अक्षरों को इटैलिक करने के लिए निम्नलिखित में से किस कीबोर्ड शॉर्टकट कुंजी का उपयोग किया जाता है?"
            opts = ["Ctrl + I", "Ctrl + B", "Ctrl + U", "Ctrl + V"]
            ans = "Ctrl + I"
        elif i == 47:
            q_eng = "Which of the following keyboard shortcuts is used to hide a row in MS-Excel 2019?"
            q_hin = "MS-Excel 2019 में एक पंक्ति को छिपाने के लिए निम्नलिखित में से किस कीबोर्ड शॉर्टकट का उपयोग किया जाता है?"
            opts = ["Ctrl + 9", "Ctrl + 0", "Ctrl + 1", "Ctrl + 2"]
            ans = "Ctrl + 9"
        elif i == 48:
            q_eng = "A sports teacher recorded scores in Excel 2019. He wants to find total scores. Which function should he use?"
            q_hin = "एक खेल शिक्षक ने MS-Excel 2019 में अंक दर्ज किए। अब वह कुल अंक ज्ञात करना चाहता है। उसे किस फंक्शन का उपयोग करना चाहिए?"
            opts = ["COUNT", "ADD", "SUM", "TOTAL"]
            ans = "SUM"
        elif i == 49:
            q_eng = "A teacher wants to arrange student marks in ascending order. Which option within Data tab should she use?"
            q_hin = "एक शिक्षिका MS-Excel 2019 में डेटा को आरोही क्रम में व्यवस्थित करना चाहती है। उसे किस विकल्प का उपयोग करना चाहिए?"
            opts = ["Sort (सॉर्ट)", "Format", "Filter", "Design"]
            ans = "Sort (सॉर्ट)"
        elif i == 50:
            q_eng = "Sirish wants to find his average marks of six subjects in Excel 2019. Which function should he use?"
            q_hin = "सिरीश छह अलग-अलग विषयों के लिए अपना औसत ज्ञात करना चाहता है। उसे MS-Excel 2019 के किस फ़ंक्शन का उपयोग करना चाहिए?"
            opts = ["Avg", "Average", "Mean", "Mode"]
            ans = "Average"
        elif i == 51:
            q_eng = "Which of the following may come from a malicious website or added intentionally along with genuine software?"
            q_hin = "निम्नलिखित में से कौन-sa वास्तविक सॉफ़्टवेयर के साथ शामिल हो सकता है, और किसी दुर्भावनापूर्ण वेबसाइट से आ सकता है?"
            opts = ["Spyware (स्पायवेयर)", "VMware", "Middleware", "Adware"]
            ans = "Spyware (स्पायवेयर)"
        elif i == 52:
            q_eng = "Which of the following keyboard shortcuts is used to select an entire column in MS-Excel 2019?"
            q_hin = "MS-Excel 2019 में संपूर्ण कॉलम का चयन करने के लिए निम्नलिखित में से किस कीबोर्ड शॉर्टकट कुंजी का उपयोग किया जाता है?"
            opts = ["Ctrl + Spacebar", "Alt + Spacebar", "Shift + Spacebar", "Spacebar"]
            ans = "Ctrl + Spacebar"

    # --- READING COMPREHENSION SECTION (Q53 to Q57) ---
    elif i <= 57:
        sect = "Reading Comprehension (Passage-Based)"
        if i == 53:
            q_eng = "According to the passage, children living in nuclear families tend to miss their:"
            q_hin = "दिए गए गद्यांश के अनुसार, एकल (मूल) परिवारों के बच्चे किसकी कमी महसूस करते हैं?"
            opts = ["parents' attention", "aunts and uncles", "grandparents' affection (स्नेह)", "native place"]
            ans = "grandparents' affection (स्नेह)"
        elif i == 54:
            q_eng = "The wisdom of old people is real and not bookish implies that grandparents got their wisdom:"
            q_hin = "वृद्ध लोगों का ज्ञान वास्तविक है किताबी नहीं। इसका मतलब है कि दादा-दादी को अपना ज्ञान:"
            opts = ["from books read", "from actual experiences in life (वास्तविक अनुभव से)", "by following traditions", "by memorising lessons"]
            ans = "from actual experiences in life (वास्तविक अनुभव से)"
        elif i == 55:
            q_eng = "How do grandparents provide a vital link between generations?"
            q_hin = "दादा-दादी, पीढ़ियों के बीच एक महत्वपूर्ण कड़ी कैसे प्रदान करते हैं?"
            opts = ["By arranging meetings", "By talking about family and showing pictures (तस्वीर दिखाकर)", "By forcing everyone to live together", "By traveling"]
            ans = "By talking about family and showing pictures (तस्वीर दिखाकर)"
        elif i == 56:
            q_eng = "Grandparents provide their grandchildren with a sense of security by:"
            q_hin = "दादा-दादी अपने पोते-पोतियों को सुरक्षा की भावना कैसे प्रदान करते हैं?"
            opts = ["teaching hard work", "comforting and being with them in difficult times (मुश्किल समय में साथ रहकर)", "serving hot food", "teaching special days"]
            ans = "comforting and being with them in difficult times (मुश्किल समय में साथ रहकर)"
        elif i == 57:
            q_eng = "Which of the following statements is FALSE as per the given passage?"
            q_hin = "दिए गए गद्यांश के अनुसार निम्नलिखित में से कौन सा कथन गलत है?"
            opts = ["Grandparents give love", "Grandparents can be good friends", "Grandparents do not know proper way of celebrating festivals", "Children learn patience"]
            ans = "Grandparents do not know proper way of celebrating festivals"

    # --- QUANTITATIVE APTITUDE SECTION (Q58 to Q63) ---
    elif i <= 63:
        sect = "Quantitative Aptitude (Maths)"
        if i == 58:
            q_eng = "What approximate value should come in place of question mark? 1002 / 49 * 99 - 1299 = ?"
            q_hin = "निम्नलिखित समीकरण में प्रश्न चिह्न (?) के स्थान पर लगभग कितना मान आना चाहिए? 1002 ÷ 49 × 99 - 1299 = ?"
            opts = ["700", "600", "900", "250"]
            ans = "700"
        elif i == 59:
            q_eng = "What approximate value should come in place of the question mark (?) in: 543 * (15/28) * (7/19) * (3/5) = ?"
            q_hin = "निम्नलिखित समीकरण में प्रश्न चिह्न (?) के स्थान पर क्या लगभग मान आना चाहिए? 543 का (15/28) का (7/19) का (3/5) = ?"
            opts = ["88", "44", "72", "64"]
            ans = "64"
        elif i == 60:
            q_eng = "In the given question, solve equations and choose correct relationship: I. 3x^2 - 13x + 12 = 0, II. 2y^2 - 15y + 28 = 0"
            q_hin = "दोनों समीकरणों को हल करते हुए उपयुक्त विकल्प का चयन करें: I. 3x^2 - 13x + 12 = 0, II. 2y^2 - 15y + 28 = 0"
            opts = ["x >= y", "Relationship cannot be determined", "x > y", "x < y"]
            ans = "x < y"
        elif i == 61:
            q_eng = "35% of a number is two times 75% of another number. What is the ratio of first number to second?"
            q_hin = "एक संख्या का 35% दूसरी संख्या के 75% का दोगुना है। पहली संख्या का दूसरी संख्या से अनुपात ज्ञात करें।"
            opts = ["35:6", "31:7", "23:7", "30:7"]
            ans = "30:7"
        elif i == 62:
            q_eng = "Positive difference between square of AM and square of GM of two numbers is 36. Find difference between AM of squares and square of AM."
            q_hin = "दो अलग संख्याओं के समांतर माध्य के वर्ग और उनके गुणोत्तर माध्य के वर्ग का अंतर 36 है। उनके वर्गों के समांतर माध्य और समांतर माध्य के वर्ग का अंतर क्या होगा?"
            opts = ["36", "24", "18", "12"]
            ans = "36"
        elif i == 63:
            q_eng = "In an exam, passed candidates were 4 times failed ones. If 35 candidates less appeared and 9 more failed, ratio would be 2:1. Total candidates were:"
            q_hin = "एक परीक्षा में उत्तीर्ण होने वाले अभ्यर्थियों की संख्या अनुत्तीर्ण से 4 गुना थी। यदि कुल 35 अभ्यर्थी कम होते और 9 अधिक अनुत्तीर्ण होते, तो अनुपात 2:1 होता। कुल अभ्यर्थी:"
            opts = ["155", "145", "140", "135"]
            ans = "135"

    # --- GENERAL MENTAL ABILITY & REASONING SECTION (Q64 to Q69) ---
    elif i <= 69:
        sect = "General Mental Ability & Reasoning"
        if i == 64:
            q_eng = "'Door' is related to 'Bang' in the same way as 'Chain' is related to:"
            q_hin = "दरवाजे (Door)' का 'बैंग (Bang)' से वही संबंध है जो 'चेन (Chain)' का किससे संबंध है?"
            opts = ["Thunder", "Clinch", "Tinkle", "Clank (क्लैंक)"]
            ans = "Clank (क्लैंक)"
        elif i == 65:
            q_eng = "Rearrange letters 'HDMEILSO' to make a meaningful 8-letter word, and select option with the last letter."
            q_hin = "नीचे दिए गए अक्षरों को पुनर्व्यवस्थित करके एक सार्थक 8 अक्षर वाला शब्द बनाएं, और शब्द का अंतिम अक्षर वाला विकल्प चुनें।"
            opts = ["M", "L", "H", "S"]
            ans = "S"
        elif i == 66:
            q_eng = "Six people D, F, G, K, S, V facing north. Exactly 2 left of V. G immediate right of V. S second right of G. F immediate left of D. Left of K is:"
            q_hin = "छह लोग उत्तर की ओर मुंह करके बैठे हैं। V के बाईं ओर ठीक दो लोग हैं। G, V के तुरंत दाईं ओर है। S, G के दाईं ओर दूसरे स्थान पर है। F, D के तुरंत बाईं ओर है। K के बाएं कितने हैं?"
            opts = ["None (कोई नहीं)", "One (एक)", "Three (तीन)", "Four (चार)"]
            ans = "None (कोई नहीं)"
        elif i == 67:
            q_eng = "Identify the figure from options which when put in place of question mark (?) will logically complete the series."
            q_hin = "विकल्पों में दी गई उस आकृति को पहचानिए जिसे प्रश्न चिह्न (?) के स्थान पर रखने पर श्रृंखला तार्किक रूप से पूरी हो जाएगी?"
            opts = ["Pattern Alpha", "Pattern Beta", "Pattern Gamma", "Pattern Delta"]
            ans = "Pattern Alpha"
        elif i == 68:
            q_eng = "What should come in place of the question mark (?) in the given series? 17, 28, 39, 50, 61, ?"
            q_hin = "दी गई श्रृंखला में प्रश्न चिह्न (?) के स्थान पर क्या आना चाहिए? 17, 28, 39, 50, 61, ?"
            opts = ["72", "70", "80", "75"]
            ans = "72"
        elif i == 69:
            q_eng = "Four letter-clusters have been given below. Three are alike in some manner and one is different. Select the different one."
            q_hin = "नीचे चार अक्षर-समूह दिए गए हैं। अंग्रेजी वर्णमाला क्रम के आधार पर असंगत अक्षर-समूह का चयन कीजिए।"
            opts = ["XZCG", "OQTX", "IMNQ", "EGJN"]
            ans = "XZCG"

    # --- GENERAL AWARENESS SECTION (Q70 to Q75) ---
    else:
        sect = "General Awareness (GK)"
        if i == 70:
            q_eng = "Haldia refinery is located in:"
            q_hin = "हल्दिया रिफाइनरी कहाँ स्थित है?"
            opts = ["West Bengal (पश्चिम बंगाल)", "Bihar", "Andhra Pradesh", "Odisha"]
            ans = "West Bengal (पश्चिम बंगाल)"
        elif i == 71:
            q_eng = "Which of the following is NOT a football club?"
            q_hin = "निम्न में से कौन-sa, एक फुटबॉल क्लब नहीं है?"
            opts = ["Arsenal", "Aston Villa", "Chelsea", "McLaren (मैकलारेन)"]
            ans = "McLaren (मैकलारेन)"
        elif i == 72:
            q_eng = "Pandit Shiv Kumar Sharma is an exponent of:"
            q_hin = "पंडित शिव कुमार शर्मा किसके प्रतिपादक (exponent) हैं?"
            opts = ["Mandolin", "Santoor (संतूर)", "Sitar", "Veena"]
            ans = "Santoor (संतूर)"
        elif i == 73:
            q_eng = "Devaluation usually causes the internal prices to:"
            q_hin = "अवमूल्यन के कारण प्रायः आंतरिक कीमतों पर क्या प्रभाव होता है?"
            opts = ["Fall", "Rise (इसमें वृद्धि होती है)", "Remain unchanged", "Fluctuate"]
            ans = "Rise (इसमें वृद्धि होती है)"
        elif i == 74:
            q_eng = "The diameter of a colloidal particle ranges from:"
            q_hin = "एक कोलॉइडी कण का व्यास किस परास (रेंज) में होता है?"
            opts = ["10^-9 m to 10^-6 m", "10^-6 m to 10^-3 m", "10^-12 m to 10^-9 m", "10^-3 m to 10^-6 m"]
            ans = "10^-9 m to 10^-6 m"
        elif i == 75:
            q_eng = "Vote on account is the permission to withdraw money from consolidated fund of India usually for how many months?"
            q_hin = "वोट ऑन अकाउंट (Vote on account) भारत की समेकित निधि से धन निकालने की अनुमति है, जो आमतौर पर दो महीने तक होती है।"
            opts = ["1 month", "2 months (दो महीने)", "3 months", "6 months"]
            ans = "2 months (दो महीने)"
            
    quiz_data.append({"section": sect, "q_eng": q_eng, "q_hin": q_hin, "options": opts, "answer": ans})

# --- 3. SESSION STATE TRACKING ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.quiz_over = False
    st.session_state.locked_questions = [False] * len(quiz_data)
    st.session_state.user_choices = [None] * len(quiz_data)

# ---- A. NEON GLOW LOGIN SCREEN ----
if not st.session_state.logged_in:
    st.markdown('<div class="main-card"><div class="header-text">👑 ANEESH CPCT QU. QUIZ </div><div class="gold-line"></div><p style="color:#ffd700; letter-spacing:3px; font-weight:bold;">⚡ CPCT TEST LOGIN ⚡</p></div>', unsafe_allow_html=True)
    
    user = st.text_input("👤 Username", placeholder="Enter name...")
    pwd = st.text_input("🔑 Password", type="password", placeholder="Enter password...")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("ENTER QUIZ 🚀"):
        if user == "Aneesh" and pwd == "626069":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid Credentials!")

# ---- B. ACTUAL ACTIVE QUIZ ARENA ----
else:
    if st.sidebar.button("Logout 🚪"):
        st.session_state.logged_in = False
        st.rerun()
    if st.sidebar.button("Reset Exam 🔄"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.quiz_over = False
        st.session_state.locked_questions = [False] * len(quiz_data)
        st.session_state.user_choices = [None] * len(quiz_data)
        st.rerun()

    # Results System
    if st.session_state.quiz_over:
        st.markdown('<div class="main-card"><div class="header-text">🏆 TEST RESULTS 🏆</div></div>', unsafe_allow_html=True)
        total_qs = len(quiz_data)
        final_score = st.session_state.score
        
        st.metric(label="Aapka Total Score", value=f"{final_score} / {total_qs}")
        
        if final_score >= 38:  
            st.balloons()
            st.success(f"👑 MUBARAK HO! Aapने Quiz Clear kar liya! Absolute Champion!")
        else:
            st.error("😥 Pass hone ke liye 38 marks zaroori hain. Fir se koshish kijiye!")
            
        if st.button("🔄 Restart Quiz "):
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.quiz_over = False
            st.session_state.locked_questions = [False] * len(quiz_data)
            st.session_state.user_choices = [None] * len(quiz_data)
            st.rerun()

    # Active Live Question Layout
    else:
        current_q = quiz_data[st.session_state.q_index]
        is_current_locked = st.session_state.locked_questions[st.session_state.q_index]
        
        st.markdown(f'<div class="main-card"><div class="section-badge">🎯 {current_q["section"]}</div><div class="header-text">CPCT-TEST-PAPER</div></div>', unsafe_allow_html=True)
        
        st.write(f"**Question {st.session_state.q_index + 1} of {len(quiz_data)}**")
        st.progress((st.session_state.q_index) / len(quiz_data))
        
        st.markdown(f'<div class="question-box"><b>EN:</b> {current_q["q_eng"]}<div class="hindi-text"><b>HI:</b> {current_q["q_hin"]}</div></div>', unsafe_allow_html=True)
        
        current_saved_choice = st.session_state.user_choices[st.session_state.q_index]
        radio_index = current_q["options"].index(current_saved_choice) if current_saved_choice in current_q["options"] else None
        
        choice = st.radio(
            "Sahi jawab chuniye / Choose correct option:", 
            current_q["options"], 
            index=radio_index, 
            key=f"q_{st.session_state.q_index}",
            disabled=is_current_locked
        )
        
        st.write("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.q_index > 0:
                if st.button("⬅️ Previous Question"):
                    st.session_state.q_index -= 1
                    st.rerun()
                    
        with col2:
            if not is_current_locked:
                if st.button("🔒 Lock Answer"):
                    if choice is not None:
                        st.session_state.user_choices[st.session_state.q_index] = choice
                        st.session_state.locked_questions[st.session_state.q_index] = True
                        if choice == current_q["answer"]:
                            st.session_state.score += 1
                        st.rerun()
                    else:
                        st.warning("Kripya pehle ek option select kijiye!")
            else:
                if current_saved_choice == current_q["answer"]:
                    st.success(f"🎉 Sahi Jawab! (+1 Mark)")
                else:
                    st.error(f"❌ Galat Jawab! Aapने '{current_saved_choice}' chuna tha. Sahi Answer tha: {current_q['answer']}")
                    
                if st.button("Next Question ➡️"):
                    if st.session_state.q_index < len(quiz_data) - 1:
                        st.session_state.q_index += 1
                    else:
                        st.session_state.quiz_over = True
                    st.rerun()
