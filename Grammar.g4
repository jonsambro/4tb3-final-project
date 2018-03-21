grammar Parralelize;

@header {
package cas.cs4tb3.parser;

import cas.cs4tb3.MIDIHelper;
import java.util.ArrayList;

}

@members {
private MIDIHelper midi = new MIDIHelper();
private long time = 0;
private int currentTempo = 120;
}

//Start rule
program: instrumentBlock* EOF {midi.saveSequence();};

scopeHeader returns [int instrumentID, int tempo]
            : INSTRUMENT('@'NUMBER)?
            {
                $instrumentID = midi.getInstrumentId($INSTRUMENT.text);
                if ($NUMBER.int > 0)
                    $tempo = $NUMBER.int;
                else $tempo = this.currentTempo;
            };

instrumentBlock
    : scopeHeader
    {
            midi.setInstrument($scopeHeader.instrumentID,time);
            if ($scopeHeader.tempo != this.currentTempo){
                this.currentTempo = $scopeHeader.tempo;
                midi.setTempo(this.currentTempo, this.time);
            }
    }
    '{'(playStatement|waitStatement)*'}'
    ;

playStatement locals [ArrayList<Integer> list = new ArrayList<Integer>()]
    : 'play'b=note(','a=note
    {
        $list.add($a.n);
    })*
    'for'duration';'
    {
        $list.add($b.n);
        for(Integer n : $list){
            midi.play(n,time,time+$duration.d);
        }
        time += $duration.d;
    };

waitStatement: 'wait''for'duration';' {time += $duration.d;};

duration returns [long d]
    : NUMBER {$d = midi.getDurationInTicks($NUMBER.int);}
    |FLOATING_NUMBER {$d = midi.getDurationInTicks(Double.parseDouble($FLOATING_NUMBER.text));};

note returns [int n]
    : noteName SHARP_FLAT? NUMBER
    {
        $n = 12*$NUMBER.int;
        $n += $noteName.noteNumber;
        if ($SHARP_FLAT.text != null){
            if ($SHARP_FLAT.text.equals("#"))
                $n++;
            else if ($SHARP_FLAT.text.equals("_"))
                $n--;
        }

    };

noteName returns [int noteNumber]
    : 'c' {$noteNumber = 0;}
    | 'd' {$noteNumber = 2;}
    | 'e' {$noteNumber = 4;}
    | 'f' {$noteNumber = 5;}
    | 'g' {$noteNumber = 7;}
    | 'a' {$noteNumber = 9;}
    | 'b' {$noteNumber = 11;};



SHARP_FLAT : '#'|'_';
RESERVED_WORD : 'play' | 'for' | 'wait';
NOTENAME: [a-g];
INSTRUMENT: [a-zA-Z]+;
NUMBER : [0-9]+ ;
FLOATING_NUMBER: ([0-9]*[.])?[0-9]+ ;
WS : [ \t\n\r]+ -> skip;
