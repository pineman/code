# @param {String} s
# @return {Boolean}
def is_valid(s)
    st = []
    s.chars.each { |c|
        if ["(", "[", "{"].include?(c)
            st.push(c)
        else
            must = case c
            when ")"
                "("
            when "]"
                "["
            when "}"
                "{"
            end
            return false unless must == st.pop
        end
    }
    return st.size == 0
end
