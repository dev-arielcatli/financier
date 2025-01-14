export type Expense = Readonly<{
  id: string;
  name: string;
  description: string;
  quantity: number;
  amount: number;
  date: Date;
  createdAt: Date;
  updatedAt: Date;
  address: string;
  tags: string[];
}>;

export type SafeDisplayExpense = Readonly<{
  id: string;
  createdAt: Date;
  updatedAt: Date;
  name: string;
  description: string;
  quantity: number;
  amount: number;
  date: Date;
  address: string;
  // TODO: Forms have issues with this model
  tags: any;
  total: number;
}>;

export type NewExpense = Readonly<{
  name: string;
  description: string;
  quantity: number;
  amount: number;
  date: string;
  address: string;
  // TODO: Forms have issues with this model
  tags: any;
}>;
