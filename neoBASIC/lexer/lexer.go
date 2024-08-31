package lexer

type Lexer struct {
	input        string
	position     int  // Current position in input (points to current chat)
	readPosition int  // Current reading position in input (after current char)
	ch           byte // Current char inder examination
}

func New(input string) *Lexer {
	l := &Lexer{input: input}
	return l
}

func (l *Lexer) readChar() {
	if l.readPosition >= len(l.input) {
		l.ch = 0
	} else {
		l.ch = l.input[l.readPosition]
	}
	l.position = l.readPosition
	l.readPosition += 1
}
