package win.pineman.first;

import java.util.List;
import java.util.Optional;

// A DAO implementation must have some type of storage of objects of type T, indexed by an id.
public interface DAO<T> {

    Optional<T> get(int id);

    List<T> getAll();

    void save(T t);

    void update(T t, String[] params);

    void delete(T t);
}
