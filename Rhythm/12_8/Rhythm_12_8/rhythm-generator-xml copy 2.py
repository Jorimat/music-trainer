#Generate Rhythm Exercise
# 8/8

import numpy as np
import functions as func


#Input
fileOut = 'test2.musicxml'

beats = 4
beat_type = 4
nsub = 8 
nhitsmin = 2

#beats = 12
#beat_type = 8
#nsub = 12 
#nhitsmin = 2



#Generate rhythm

nhits = np.random.choice(range(nhitsmin, nsub))
hits = np.random.choice(range(nsub), nhits, replace=False)


#hits = np.array([0,1,2,4])
#hits = np.array([0,1,3])
#hits = np.array([1,3])
#hits = np.array([1,3,5,7])
#hits = np.array([0,1,2,3,4,5,6,7])
#hits = np.array([])
#hits = np.array([2, 0, 6, 4, 3, 5, 1])


#hits = np.array(['1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0'])

print(hits)


rhythm = []
for i in range(nsub):
    if i in hits:
        rhythm.append('1')
    else:
        rhythm.append('0')
print (rhythm)   



# Make subgroups

def regroup(l):
    for sub in l:
        flattened = func.flatten(sub)
        if len(set(flattened)) == 1:
            grouped.append(''.join(flattened))
        elif type(sub) == list:
            regroup(sub)


nested = func.nest(rhythm)
grouped = []
regroup(nested)
      
      
print(grouped)






#print(func.group(rhythm))
#rhythm = func.group(rhythm)
#print (rhythm)   



#Generate xml

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
        <divisions>2</divisions>
        <key>
          <fifths>0</fifths>
          </key>
'''
out += '''<time>
          <beats>{}</beats>
          <beat-type>{}</beat-type>
          </time>
'''.format(beats, beat_type)

out += '''<clef>
          <sign>F</sign>
          <line>4</line>
          </clef>
        </attributes>
'''

for item in grouped:
    print(item)

    if item == '0':
        out += '''        <note>
                <rest/>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
                </note>
        '''   
    
    elif item == '1':
        out += '''        <note default-x="94.23" default-y="-25.00">
                <pitch>
                  <step>C</step>
                  <octave>3</octave>
                  </pitch>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
                <stem>up</stem>
                </note>
        '''
        
    elif item == '00':
        out += '''        <note>
                <rest/>
                <duration>2</duration>
                <voice>1</voice>
                <type>quarter</type>
                </note>
        '''           

    elif item == '11':
        out += '''        <note default-x="94.23" default-y="-25.00">
                <pitch>
                  <step>C</step>
                  <octave>3</octave>
                  </pitch>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
                <stem>up</stem>
                <beam number="1">begin</beam>
                </note>
                <note default-x="94.23" default-y="-25.00">
                <pitch>
                  <step>C</step>
                  <octave>3</octave>
                  </pitch>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
                <stem>up</stem>
                <beam number="1">end</beam>
                </note>
        '''

        
    elif item == '0000':
        out += '''        <note>
                <rest/>
                <duration>4</duration>
                <voice>1</voice>
                <type>half</type>
                </note>
        '''    
 
    elif item == '1111':
        out += '''        <note default-x="94.23" default-y="-25.00">
                <pitch>
                  <step>C</step>
                  <octave>3</octave>
                  </pitch>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
                <stem>up</stem>
                </note>
                <note default-x="94.23" default-y="-25.00">
                <pitch>
                  <step>C</step>
                  <octave>3</octave>
                  </pitch>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
                <stem>up</stem>
                </note>
                <note default-x="94.23" default-y="-25.00">
                <pitch>
                  <step>C</step>
                  <octave>3</octave>
                  </pitch>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
                <stem>up</stem>
                </note>
                <note default-x="94.23" default-y="-25.00">
                <pitch>
                  <step>C</step>
                  <octave>3</octave>
                  </pitch>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
                <stem>up</stem>
                <beam number="1">end</beam>
                </note>'''   
        
        
    elif item == '111111':
        for i in range(6):
            out += '''        <note default-x="94.23" default-y="-25.00">
                    <pitch>
                      <step>C</step>
                      <octave>3</octave>
                      </pitch>
                    <duration>1</duration>
                    <voice>1</voice>
                    <type>eighth</type>
                    </note>'''    
        

    elif item == '00000000':
        out += '''        <note>
                <rest/>
                <duration>4</duration>
                <voice>1</voice>
                <type>whole</type>
                </note>
        '''            

    
out += '''<barline location="right">
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
