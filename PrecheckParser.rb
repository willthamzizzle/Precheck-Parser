# !/bin/env ruby

# Author: William Thammavong
# Date: 08/07/2015
# Will be given input text file containing Pre check health check.
# That text file will then get parsed into a more friendly manner to input to notes.


textFileInput = ARGV[0]
textFileOutput = ARGV[1]

if (textFileInput != nil)
  inputText = File.open(textFileInput)
else
  puts 'You have not specified a text file as the first argument.'
end









puts inputText.read()

puts textFileOutput
puts textFileInput
