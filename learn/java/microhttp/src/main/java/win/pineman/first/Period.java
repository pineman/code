package win.pineman.first;

import java.util.Date;

/** Effective Java Item 50, mutable things inside immutable class.
 * Be aware that java.util.Date is obsolete!
 */
public final class Period {
    private final Date start;
    private final Date end;

    /**
     * Repaired constructor - makes defensive copies of parameters
     */
    // (Date is a mutable class!!)
    public Period(Date start, Date end) {
        this.start = new Date(start.getTime());
        this.end = new Date(end.getTime());
        if (this.start.compareTo(this.end) > 0)
            throw new IllegalArgumentException(this.start + " after " + this.end);
    }

    public Date start() { return start; }
    public Date end() { return end; }
}