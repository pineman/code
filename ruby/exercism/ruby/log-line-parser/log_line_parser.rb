class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    @line.sub(/\[.*?\]: /, '').strip()
  end

  def log_level
    @line[/\[(.*?)\]/, 1].downcase
    #/\[([^\]]*)\]/.match(@line)[1].downcase
  end

  def reformat
    "#{message} (#{log_level})"
  end
end
