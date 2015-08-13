# !/bin/env ruby

# Author: William Thammavong
# Date: 08/07/2015
# Will be given input text file containing pre check health check for various Avamar grids.
# That text file will then get parsed into a more friendly manner to input to notes.


$textFileInput = ARGV[0]


def obtainText()

  inputText = nil
  if(File.exist?($textFileInput))
    inputText = File.open($textFileInput)
  end

  #puts inputText.read()
  return inputText
end


def parsePrecheck()

  theText = obtainText()
  puts text.read()
end


parsePrecheck()
