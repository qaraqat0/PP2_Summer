CREATE OR REPLACE PROCEDURE upsert_contact(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE first_name = p_name
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO contacts(first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_contacts(p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    ii INT;
BEGIN
    FOR ii IN 1..array_length(p_names, 1) LOOP
        CALL upsert_contact(p_names[ii], p_phones[ii]);
    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE first_name = p_value
       OR phone = p_value;
END;
$$;