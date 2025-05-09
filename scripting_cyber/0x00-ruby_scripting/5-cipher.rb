#!/usr/bin/env ruby
class CaesarCipher
  @@UPPERCASE_LETTERS = ("A".."Z").to_a
  @@LOWERCASE_LETTERS = ("a".."z").to_a

  attr_accessor :shift

  def initialize(shift)
    @shift = shift
  end

  def encrypt(message)
    encrypted = ""
    message.split("").to_a.each do |x|
      if @@UPPERCASE_LETTERS.include? x
        encrypted += @@UPPERCASE_LETTERS[ (@@UPPERCASE_LETTERS.index(x) + @shift) % 26]
      elsif @@LOWERCASE_LETTERS.include? x
        encrypted += @@LOWERCASE_LETTERS[ (@@LOWERCASE_LETTERS.index(x) + @shift) % 26]
      else
        encrypted += x
      end
    end
    return encrypted
  end

  def decrypt(message)
    decrypted = ""
    message.split("").to_a.each do |x|
      if @@UPPERCASE_LETTERS.include? x
        decrypted += @@UPPERCASE_LETTERS[ (@@UPPERCASE_LETTERS.index(x) - @shift) % 26]
      elsif @@LOWERCASE_LETTERS.include? x
        decrypted += @@LOWERCASE_LETTERS[ (@@LOWERCASE_LETTERS.index(x) - @shift) % 26]
      else
        decrypted += x
      end
    end
    return decrypted
  end

  private

  def cipher(message, shift)
    encrypted = encrypt(message)
    decrypted = decrypt(encrypted)
    puts "Encrypted message: #{encrypted}"
    puts "Decrypted message: #{decrypted}"
  end
end
