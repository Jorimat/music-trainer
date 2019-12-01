# Generate Rhythm Exercise
# 4/4 in 16ths
# 4 16th patterns repeating
# Combination of two bars


import numpy as np
#import functions as func


# Input
fileOut = 'score-16-16-easy-nbar.musicxml'
bars = 4
beats = 4
beat_type = 4
divisions = 4




# Patterns to chose from

pattern = ['''    
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>''',

               '''    
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>           
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>''',

               '''    
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>  
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>    
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>''',

               '''    
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>        
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>  
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>''',

               '''    
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>               
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>  
        <note default-x="94.23" default-y="-25.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type></note>''',

'''
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>
        <note default-x="161.22" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">end</beam><beam number="2">end</beam></note>
        <note><rest/><duration>2</duration><voice>1</voice><type>eighth</type></note>''',         

'''
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>   
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>
        <note default-x="161.22" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">end</beam><beam number="2">end</beam></note>
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>''',   

'''
        <note><rest/><duration>2</duration><voice>1</voice><type>eighth</type></note>
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>
        <note default-x="161.22" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">end</beam><beam number="2">end</beam></note>''',

'''
        <note default-x="161.22" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">end</beam><beam number="2">end</beam></note>
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>   
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>   
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>''',          

'''
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>   
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>''',  

'''
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>   
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>  
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>''',

'''
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>
        <note><rest/><duration>2</duration><voice>1</voice><type>eighth</type></note>      
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>''',  

'''
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>  
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>
        <note><rest/><duration>2</duration><voice>1</voice><type>eighth</type></note>''',  

'''
        <note><rest/><duration>2</duration><voice>1</voice><type>eighth</type></note>      
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>''',  

'''
        <note><rest/><duration>2</duration><voice>1</voice><type>eighth</type></note>      
        <note><rest/><duration>1</duration><voice>1</voice><type>16th</type></note>  
        <note default-x="94.23" default-y="-15.00"><pitch><step>C</step><octave>3</octave></pitch><duration>1</duration><voice>1</voice><type>16th</type><stem>up</stem><beam number="1">begin</beam><beam number="2">begin</beam></note>'''           
]



# Select patterns
sel = np.random.choice(range(len(pattern)), bars, replace=False)

print(sel)



#Generate xml string

out = ''

out += '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <identification>
    <encoding>
      <software>MuseScore 3.2.3</software>
      <encoding-date>2019-07-28</encoding-date>
      <supports element="accidental" type="yes"/>
      <supports element="beam" type="yes"/>
      <supports element="print" attribute="new-page" type="yes" value="yes"/>
      <supports element="print" attribute="new-system" type="yes" value="yes"/>
      <supports element="stem" type="yes"/>
      </encoding>
    </identification>
  <defaults>
    <scaling>
      <millimeters>7.05556</millimeters>
      <tenths>40</tenths>
      </scaling>
    <page-layout>
      <page-height>1683.78</page-height>
      <page-width>1190.55</page-width>
      <page-margins type="even">
        <left-margin>56.6929</left-margin>
        <right-margin>56.6929</right-margin>
        <top-margin>56.6929</top-margin>
        <bottom-margin>113.386</bottom-margin>
        </page-margins>
      <page-margins type="odd">
        <left-margin>56.6929</left-margin>
        <right-margin>56.6929</right-margin>
        <top-margin>56.6929</top-margin>
        <bottom-margin>113.386</bottom-margin>
        </page-margins>
      </page-layout>
    <word-font font-family="FreeSerif" font-size="10"/>
    <lyric-font font-family="FreeSerif" font-size="11"/>
    </defaults>
  <part-list>
    <score-part id="P1">
      <part-name>Music</part-name>
      <score-instrument id="P1-I1">
        <instrument-name></instrument-name>
        </score-instrument>
      <midi-device id="P1-I1" port="1"></midi-device>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>1</midi-program>
        <volume>78.7402</volume>
        <pan>0</pan>
        </midi-instrument>
      </score-part>
    </part-list>
  <part id="P1">
    <measure number="1" width="564.88">
      <print>
        <system-layout>
          <system-margins>
            <left-margin>0.00</left-margin>
            <right-margin>512.29</right-margin>
            </system-margins>
          <top-system-distance>170.00</top-system-distance>
          </system-layout>
        </print>
      <barline location="left">
        <bar-style>heavy-light</bar-style>
        <repeat direction="forward"/>
        </barline>
      <attributes>
        <divisions>{}</divisions>
        <key>
          <fifths>0</fifths>
          </key>
'''.format(divisions)

out += '''        <time>
          <beats>{}</beats>
          <beat-type>{}</beat-type>
          </time>
'''.format(beats, beat_type)

out += '''        <clef>
          <sign>F</sign>
          <line>4</line>
          </clef>
      </attributes>
      <direction placement="above">
        <direction-type>
          <words default-x="-49.33" relative-y="20.00" font-weight="bold" font-size="12">Lento</words>
          </direction-type>
        <sound tempo="52.5"/>
        </direction>      
'''


s = 0
for i in range(4):
    out += pattern[sel[s]]
out += '''
    </measure>
    '''
    
    

for s in range(1, bars-1):
    out += '''    
    <measure number="{}" width="564.88">
        '''.format(s+1)
    for i in range(4):
        out += pattern[sel[s]]
    out += '''
    </measure>
    '''
    
    
s = bars-1
out += '''    
    <measure number="{}" width="564.88">
    '''.format(s+1)
for i in range(4):
    out += pattern[sel[s]]

    
    
    
    

out += '''
        <barline location="right">
        <bar-style>light-heavy</bar-style>
        <repeat direction="backward"/>
        </barline>
      </measure>
    </part>
  </score-partwise>
'''




#Save
file = open(fileOut,'w') 
file.write(out) 
file.close() 
hits = list(range(12))
