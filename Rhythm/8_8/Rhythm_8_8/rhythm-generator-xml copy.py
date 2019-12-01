#Generate Rhythm Exercise
# 8/8

import numpy as np


#Input
fileOut = 'test2.musicxml'
beats = 4
sub = 2 
nhitsmin = 2



#Generate rhythm

nhits = np.random.choice(range(nhitsmin, beats*sub))
hits = np.random.choice(range(beats*sub), nhits, replace=False)


#hits = np.array([0,1,2,3])
print(hits)




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
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
          </time>
        <clef>
          <sign>F</sign>
          <line>4</line>
          </clef>
        </attributes>
'''


for i in range(8):
    if i in hits:
        out += '''<note default-x="94.23" default-y="-25.00">
                <pitch>
                  <step>C</step>
                  <octave>3</octave>
                  </pitch>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
                <stem>up</stem>
        '''
        
        if i%2 == 0 and i+1 in hits:
            out += '''
                    <beam number="1">begin</beam>
                    '''
            
        if i%2 == 1 and i-1 in hits:
            out += '''
                    <beam number="1">end</beam>
                    '''           
            
        out += '''
                    </note>
            '''
        
    else:
        out += '''<note>
                <rest/>
                <duration>1</duration>
                <voice>1</voice>
                <type>eighth</type>
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
