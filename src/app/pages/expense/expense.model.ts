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
