module eu.pineman.fxproj {
    requires javafx.controls;
    requires javafx.fxml;

    opens eu.pineman.fxproj to javafx.fxml;
    exports eu.pineman.fxproj;
}