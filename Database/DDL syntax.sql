BEGIN;


CREATE TABLE IF NOT EXISTS public.authors
(
    author_id integer NOT NULL DEFAULT nextval('authors_author_id_seq'::regclass),
    author_name character varying(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT authors_pkey PRIMARY KEY (author_id)
);

CREATE TABLE IF NOT EXISTS public.books
(
    book_id integer NOT NULL DEFAULT nextval('books_book_id_seq'::regclass),
    title character varying(256) COLLATE pg_catalog."default" NOT NULL,
    author_id integer NOT NULL,
    category_id integer NOT NULL,
    total_quantity integer NOT NULL,
    CONSTRAINT books_pkey PRIMARY KEY (book_id),
    CONSTRAINT unique_title_author UNIQUE (title, author_id)
);

CREATE TABLE IF NOT EXISTS public.categories
(
    category_id integer NOT NULL DEFAULT nextval('categories_category_id_seq'::regclass),
    category_name character varying(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT categories_pkey PRIMARY KEY (category_id),
    CONSTRAINT categories_category_name_key UNIQUE (category_name)
);

CREATE TABLE IF NOT EXISTS public.libraries
(
    library_id integer NOT NULL DEFAULT nextval('libraries_library_id_seq'::regclass),
    library_name character varying(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT libraries_pkey PRIMARY KEY (library_id),
    CONSTRAINT libraries_library_name_key UNIQUE (library_name)
);

CREATE TABLE IF NOT EXISTS public.library_books
(
    library_id integer NOT NULL,
    book_id integer NOT NULL,
    CONSTRAINT library_books_pkey PRIMARY KEY (library_id, book_id)
);

CREATE TABLE IF NOT EXISTS public.loans
(
    loan_id integer NOT NULL DEFAULT nextval('loans_loan_id_seq'::regclass),
    book_id integer NOT NULL,
    user_id integer NOT NULL,
    loan_date date NOT NULL DEFAULT now(),
    due_date date NOT NULL GENERATED ALWAYS AS ((loan_date + '14 days'::interval)) STORED,
    return_date date,
    CONSTRAINT loans_pkey PRIMARY KEY (loan_id)
);

CREATE TABLE IF NOT EXISTS public.queues
(
    queue_id integer NOT NULL DEFAULT nextval('queues_queue_id_seq'::regclass),
    queue_start time without time zone NOT NULL DEFAULT now(),
    user_id integer NOT NULL,
    book_id integer NOT NULL,
    CONSTRAINT queues_pkey PRIMARY KEY (queue_id)
);

CREATE TABLE IF NOT EXISTS public.users
(
    user_id integer NOT NULL DEFAULT nextval('users_user_id_seq'::regclass),
    email character varying(256) COLLATE pg_catalog."default" NOT NULL,
    user_name character varying(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (user_id),
    CONSTRAINT users_email_key UNIQUE (email)
);

ALTER TABLE IF EXISTS public.books
    ADD CONSTRAINT books_author_id_fkey FOREIGN KEY (author_id)
    REFERENCES public.authors (author_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.books
    ADD CONSTRAINT books_category_id_fkey FOREIGN KEY (category_id)
    REFERENCES public.categories (category_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.library_books
    ADD CONSTRAINT library_books_book_id_fkey FOREIGN KEY (book_id)
    REFERENCES public.books (book_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.library_books
    ADD CONSTRAINT library_books_library_id_fkey FOREIGN KEY (library_id)
    REFERENCES public.libraries (library_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.loans
    ADD CONSTRAINT loans_book_id_fkey FOREIGN KEY (book_id)
    REFERENCES public.books (book_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.loans
    ADD CONSTRAINT loans_user_id_fkey FOREIGN KEY (user_id)
    REFERENCES public.users (user_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.queues
    ADD CONSTRAINT queues_book_id_fkey FOREIGN KEY (book_id)
    REFERENCES public.books (book_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.queues
    ADD CONSTRAINT queues_user_id_fkey FOREIGN KEY (user_id)
    REFERENCES public.users (user_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

END;